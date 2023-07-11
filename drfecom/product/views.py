from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from .models import Category, Brand, Product
from .serializers import CategotySerielizer, BrandSerielizer, ProductSerielizer

# Create your views here.
class CategoryViewSet(viewsets.ViewSet):
    """
    TODO: 
        A simple viewset for viewing categories -> https://www.django-rest-framework.org/api-guide/viewsets/
        Different kinds of viewset -> https://www.django-rest-framework.org/api-guide/viewsets/#viewset-actions
    """
    questyset = Category.objects.all()

    @extend_schema(responses=CategotySerielizer)
    def list(self, request):
        serielizer = CategotySerielizer(self.questyset, many=True)
        return Response(serielizer.data)
    

class BrandViewSet(viewsets.ViewSet):
    """
    TODO: 
        A simple viewset for viewing brands -> https://www.django-rest-framework.org/api-guide/viewsets/
        Different kinds of viewset -> https://www.django-rest-framework.org/api-guide/viewsets/#viewset-actions
    """
    questyset = Brand.objects.all()

    @extend_schema(responses=BrandSerielizer)
    def list(self, request):
        serielizer = BrandSerielizer(self.questyset, many=True)
        return Response(serielizer.data)
    

class ProductViewSet(viewsets.ViewSet):
    """
    TODO: 
        A simple viewset for viewing products -> https://www.django-rest-framework.org/api-guide/viewsets/
        Different kinds of viewset -> https://www.django-rest-framework.org/api-guide/viewsets/#viewset-actions
    """
    questyset = Product.objects.all()

    @extend_schema(responses=ProductSerielizer)
    def list(self, request):
        serielizer = ProductSerielizer(self.questyset, many=True)
        return Response(serielizer.data)

