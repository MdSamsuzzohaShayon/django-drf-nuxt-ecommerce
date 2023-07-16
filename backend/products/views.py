from django.shortcuts import render
from rest_framework import generics
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

# Create your views here.
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductSerializer

class CategoryCreateView(generics.CreateAPIView):
    serializer_class = CategorySerializer
