from rest_framework import serializers

from .models import Brand, Category, Product


class CategotySerielizer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class BrandSerielizer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class ProductSerielizer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"