from rest_framework import serializers
from .models import Product, Category

# class AccountSerializer(serializers.ModelSerializer):
#     url = serializers.CharField(source='get_absolute_url', read_only=True)

#     class Meta:
#         model = Account


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        # exclude = ["id"]
    
    # def create(self, validated_data):
    #     images_data = self.context.get('view').request.FILES
    #     images = [Product(image=image_data) for image_data in images_data.values()]
    #     return Product.objects.bulk_create(images)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"