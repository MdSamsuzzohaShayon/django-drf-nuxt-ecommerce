from django.shortcuts import render
from rest_framework import generics
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer, ProductUpdateSerializer, CategoryUpdateSerializer

# Products
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    
    # def perform_create(self, serializer):
    #     instance = serializer.save()
    #     print("Category create instance(perform_create)->" + instance)

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductUpdateView(generics.UpdateAPIView):
    serializer_class = ProductUpdateSerializer
    queryset = Product.objects.all()

    def perform_update(self, serializer):
        instance = serializer.save()
        print(instance)
        if instance.title:
            del instance.title

class ProductDeleteView(generics.DestroyAPIView):
    serializer_class = ProductSerializer


# Categories
class CategoryCreateView(generics.CreateAPIView):
    serializer_class = CategorySerializer

    # def perform_create(self, serializer):
    #     name = serializer.validated_data.get('name')
    #     # instance = serializer.save(name=name)
    #     print("Category create instance(perform_create)->" + name)

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryUpdateView(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryUpdateSerializer

    def perform_update(self, serializer):
        instance = serializer.save()
        print(instance)

class CategoryDeleteView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "pk"
        
