from rest_framework import serializers
from .models import Order
from accounts.serializers import AddressSerializer

class OrderSerializer(serializers.ModelSerializer):
    # total = serializers.CharField(read_only=True)
    total = serializers.CharField(read_only=True)
    is_paid = serializers.BooleanField(read_only=True)
    
    # address = AddressSerializer(many=True, read_only=True)
    address = AddressSerializer(many=False, read_only=True)
    class Meta:
        model = Order 
        fields = ["id", "status", "is_paid", "product", "address", "quantity", "total"]


class UserOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order 
        fields = ["id", "status"]