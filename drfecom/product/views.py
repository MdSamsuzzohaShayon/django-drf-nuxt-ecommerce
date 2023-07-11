from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Category
from .serializers import CategotySerielizer

# Create your views here.
class CategoryViewSet(viewsets.ViewSet):
    """
    TODO: 
        A simple viewset for viewing categories -> https://www.django-rest-framework.org/api-guide/viewsets/
        Different kinds of viewset -> https://www.django-rest-framework.org/api-guide/viewsets/#viewset-actions
    """
    questyset = Category.objects.all()

    def list(self, request):
        serielizer = CategotySerielizer(self.questyset, many=True)
        return Response(serielizer.data)

