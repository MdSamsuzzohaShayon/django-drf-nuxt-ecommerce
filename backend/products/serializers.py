from rest_framework import serializers
from .models import Product

# class AccountSerializer(serializers.ModelSerializer):
#     url = serializers.CharField(source='get_absolute_url', read_only=True)

#     class Meta:
#         model = Account


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        # exclude = ["id"]