from django.urls import path
from .views import CreateOrderView, OrderListView, OrderListOfUserView, CancelOrderView

urlpatterns = [
    path('new/', CreateOrderView.as_view(), name="order-create"),
    path('list/', OrderListView.as_view(), name="order-list"),
    path('user/', OrderListOfUserView.as_view(), name="user-order-list"),
    path('cancel/<str:pk>/', CancelOrderView.as_view(), name="order-cancel"),
]