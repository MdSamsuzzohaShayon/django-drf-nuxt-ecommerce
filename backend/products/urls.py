from django.urls import path
from .views import ProductListView, CategoryCreateView, ProductCreateView


urlpatterns = [
    path('', ProductListView.as_view(), name="product-list"),
    path('new/', ProductCreateView.as_view(), name="product-create"),
    path('categories/', CategoryCreateView.as_view(), name='category-create')
]
