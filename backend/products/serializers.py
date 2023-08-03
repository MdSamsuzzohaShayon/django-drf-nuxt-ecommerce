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

class ProductUpdateSerializer(serializers.ModelSerializer):
    
    title = serializers.CharField(read_only=True)
    discount_price = serializers.DecimalField(max_digits=10, decimal_places=0, required=False)
    total_stock = serializers.DecimalField(max_digits=10, decimal_places=0, required=False)
    description = serializers.CharField(required=False)
    # category = TreeForeignKey(
    #     Category, related_name="product_category", on_delete=models.SET_NULL, null=True, blank=True
    # )
    # image1 = models.ImageField(upload_to=upload_to, blank=True, null=True)
    # image2 = models.ImageField(upload_to=upload_to, blank=True, null=True)
    # image3 = models.ImageField(upload_to=upload_to, blank=True, null=True)
    # image4 = models.ImageField(upload_to=upload_to, blank=True, null=True)
    # discount_price = serializers.SerializerMethodField(required=False)
    # total_stock = serializers.SerializerMethodField(required=False)
    # description = serializers.SerializerMethodField(required=False)

    class Meta:
        model = Product
        fields = "__all__"
        # exclude = ["id"]
    


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CategoryUpdateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    class Meta:
        model = Category
        fields = "__all__"