from django.urls import path
from .views import ProductListView, CategoryCreateView, ProductCreateView, ProductDetailView, ProductUpdateView, ProductDeleteView, CategoryListView, CategoryDeleteView, CategoryUpdateView


urlpatterns = [
    path('', ProductListView.as_view(), name="product-list"),
    path('new/', ProductCreateView.as_view(), name="product-create"),
    # path("product/views/", views.ProductViewsAPIView.as_view()),
    path('<int:pk>/', ProductDetailView.as_view(), name="product-detail"),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name="product-update"),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name="product-delete"),

    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/new', CategoryCreateView.as_view(), name='category-create'),
    path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category-update'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),
]
