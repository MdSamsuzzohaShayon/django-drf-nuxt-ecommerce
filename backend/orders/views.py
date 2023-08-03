import jwt
import os

from rest_framework.generics import CreateAPIView, ListAPIView
from .serializers import OrderSerializer, UserOrderSerializer
from .models import Order
from products.models import Product
from accounts.mixins import GeneralUserPermissionMixin, StaffEditorPermissionMixin
from django.shortcuts import get_object_or_404

# Create order
class CreateOrderView(GeneralUserPermissionMixin, CreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def perform_create(self, serializer):
        quantity = self.request.data.get('quantity')
        product_id = self.request.data.get('product')
        # Access product and quentity and ultiply them to get total
        product = Product.objects.get(id=product_id)
        # print(product.discount_price, quantity)
        total = product.discount_price * quantity
        serializer.save(buyer=self.request.user, total=total)
        # print(serializer.data)

class OrderListView(StaffEditorPermissionMixin, ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


# View for orders of specific user
class OrderListOfUserView(GeneralUserPermissionMixin, ListAPIView):
    serializer_class = OrderSerializer

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
