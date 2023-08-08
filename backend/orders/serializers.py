from rest_framework import serializers
from .models import Order
from accounts.serializers import AddressSerializer
from products.serializers import ProductSerializer

class OrderSerializer(serializers.ModelSerializer):
    # total = serializers.CharField(read_only=True)
    total = serializers.CharField(read_only=True)
    is_paid = serializers.BooleanField(read_only=True)
    status = serializers.CharField(read_only=True)
    class Meta:
        model = Order 
        fields = ["id", "status", "is_paid", "product", "address", "quantity", "total"]

class OrderListSerializer(serializers.ModelSerializer):
    address = AddressSerializer(many=False, read_only=True)
    product = ProductSerializer(many=False, read_only=True)
    class Meta:
        model = Order 
        fields = ["id", "status", "is_paid", "product", "address", "quantity", "total"]


class OrderCancelSerializer(serializers.ModelSerializer):
    total = serializers.CharField(read_only=True)
    is_paid = serializers.BooleanField(read_only=True)
    status = serializers.CharField(read_only=True)
    product = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    address = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    class Meta:
        model = Order 
        fields = ["id", "status", "is_paid", "product", "address", "quantity", "total"]