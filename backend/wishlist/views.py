from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from .serializers import WishlistSerializer
from .models import Wishlist
from accounts.mixins import IsStaffEditorPermission

# Create your views here.
class CreateWishlistView(CreateAPIView):
    serializer_class = WishlistSerializer
    queryset = Wishlist.objects.all()

class WishlistListView(IsStaffEditorPermission, ListAPIView):
    serializer_class = WishlistSerializer
    queryset = Wishlist.objects.all()

class UpdateWishlistView(IsStaffEditorPermission, UpdateAPIView):
    # Make sure Preview
    serializer_class = WishlistSerializer
    queryset = Wishlist.objects.all()

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.preview = True
