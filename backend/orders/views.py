import jwt
import os
import logging

from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from rest_framework.validators import ValidationError
from .serializers import OrderSerializer, OrderCancelSerializer, OrderListSerializer
from accounts.serializers import AddressSerializer
from .models import Order
from products.models import Product, DeliveryPlace
from accounts.mixins import GeneralUserPermissionMixin, StaffEditorPermissionMixin
from django.shortcuts import get_object_or_404

# Create order
class CreateOrderView(GeneralUserPermissionMixin, CreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def perform_create(self, serializer):
        print("All data ----> ",self.request.data)
        quantity = self.request.data.get('quantity')
        product_id = self.request.data.get('product')
        city_id = self.request.data.get('city')
        # Access product and quentity and ultiply them to get total
        product = Product.objects.get(id=product_id)
        city = DeliveryPlace.objects.get(id=city_id)
        # print("Get category from here ",product.category.shipping_charge)
        # print("Get price for specific city ", city.price)
        # (Price * Quantity) + {Delivery Place + Product Category Shipping Price) * Quantity}
        product_total = product.discount_price * quantity if product.discount_price else product.price
        delivery_charge = (city.price + product.category.shipping_charge) * quantity
        total = product_total + delivery_charge
        print({
            "product_total": product_total,
            "delivery_charge": delivery_charge,
            "total": total
        })
        serializer.save(buyer=self.request.user, total=total)
        # print(serializer.data)

class OrderListView(StaffEditorPermissionMixin, ListAPIView):
    serializer_class = OrderListSerializer
    queryset = Order.objects.all()


# View for orders of specific user
class OrderListOfUserView(GeneralUserPermissionMixin, ListAPIView):
    serializer_class = OrderListSerializer

    def get_queryset(self):
        decoded_token = jwt.decode(self.request.headers['Authorization'].split(' ')[1], os.getenv('JSON_TOKEN_SECRET'), algorithms=["HS256"])
        queryset = Order.objects.filter(buyer_id =decoded_token['user_id'])
        return queryset
    
    def get_object(self):
        queryset = self.get_queryset()
        filter = {}
        obj = get_object_or_404(queryset, **filter)
        return obj
    
    # Populate product and address

class CancelOrderView(GeneralUserPermissionMixin, UpdateAPIView):
    serializer_class = OrderCancelSerializer
    queryset = Order.objects.all()
    
    def perform_update(self, serializer):
        # queryset = self.get_queryset()
        
        # print(queryset)
        order_id = self.kwargs[self.lookup_field]
        
        # print(self.request.query_params, self.lookup_field, dir(self.request))
        # find_order = Order.objects.get(id=order_id)
        # if find_order:
        #     if find_order.status == 'PG':
        #         serializer.save(status="CL")
        
        try:
            queryset = Order.objects.get(id=order_id)
            if queryset.status != 'PG':
                raise ValidationError('You can not cancel this order!')
            else:
                serializer.save(status="CL")
        except Exception as e:
            logging.error(e)
            raise ValidationError('You can not cancel this order!')
