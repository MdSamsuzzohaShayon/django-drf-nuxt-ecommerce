from django.shortcuts import render
from rest_framework import generics, filters
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer, ProductUpdateSerializer, CategoryUpdateSerializer
from accounts.mixins import StaffEditorPermissionMixin, GeneralUserPermissionMixin


# Products
class ProductListSearchView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']

class ProductListFilterView(generics.ListAPIView):
    serializer_class = ProductSerializer
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        filters_kwargs = {}
        title = self.request.query_params.get('title')
        if title is not None:
            filters_kwargs['title'] = title
        price = self.request.query_params.get('price')
        if price is not None:
            filters_kwargs['price__lte'] = price
        total_stock = self.request.query_params.get('total_stock')
        if total_stock is True:
            filters_kwargs['total_stock__gt'] = 0
        category = self.request.query_params.get('category')
        if category is not None:
            filters_kwargs['category'] = category
        queryset = Product.objects.filter(**filters_kwargs)
        return queryset


class ProductCreateView(StaffEditorPermissionMixin, generics.CreateAPIView):
    queryset = queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [IsAuthenticated]
    
    # def perform_create(self, serializer):
    #     instance = serializer.save()
    #     print("Category create instance(perform_create)->" + instance)

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductUpdateView(StaffEditorPermissionMixin, generics.UpdateAPIView):
    serializer_class = ProductUpdateSerializer
    queryset = Product.objects.all()

    def perform_update(self, serializer):
        instance = serializer.save()
        print(instance)
        if instance.title:
            del instance.title

class ProductDeleteView(StaffEditorPermissionMixin, generics.DestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


# Categories
class CategoryCreateView(StaffEditorPermissionMixin, generics.CreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


    # def perform_create(self, serializer):
    #     name = serializer.validated_data.get('name')
    #     # instance = serializer.save(name=name)
    #     print("Category create instance(perform_create)->" + name)

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryUpdateView(StaffEditorPermissionMixin, generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryUpdateSerializer

    def perform_update(self, serializer):
        instance = serializer.save()
        print(instance)

class CategoryDeleteView(StaffEditorPermissionMixin, generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "pk"
        
