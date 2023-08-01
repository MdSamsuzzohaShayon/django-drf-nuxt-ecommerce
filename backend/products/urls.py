from django.urls import path
from .views import ProductListSearchView, CategoryCreateView, ProductCreateView, ProductDetailView, ProductUpdateView, ProductDeleteView, CategoryListView, CategoryDeleteView, CategoryUpdateView, ProductListFilterView, ProductsByCategory


urlpatterns = [
    path('', ProductListSearchView.as_view(), name="product-search-list"),
    path('filters/', ProductListFilterView.as_view(), name="product-filters-list"),
    path('new/', ProductCreateView.as_view(), name="product-create"),
    # path("product/views/", views.ProductViewsAPIView.as_view()),
    path('<int:pk>/', ProductDetailView.as_view(), name="product-detail"),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name="product-update"),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name="product-delete"),

    path('categories/<int:catId>', ProductsByCategory.as_view(), name='category-product-list'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/new/', CategoryCreateView.as_view(), name='category-create'),
    path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category-update'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),
]
