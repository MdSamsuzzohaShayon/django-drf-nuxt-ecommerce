from rest_framework import serializers

from .models import Brand, Category, Product


class CategotySerielizer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]

class BrandSerielizer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class ProductSerielizer(serializers.ModelSerializer):
    # Make sure name of the variable name must be the name from Product model. 
    brand = BrandSerielizer()
    category = CategotySerielizer()
    class Meta:
        model = Product
        fields = "__all__"