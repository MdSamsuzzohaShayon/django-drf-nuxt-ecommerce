from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from .serializers import ContactSerializer
from .models import Contact
from accounts.mixins import IsStaffEditorPermission

# Create your views here.
class CreateContactView(CreateAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

class ContactListView(IsStaffEditorPermission, ListAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

class UpdateContactView(IsStaffEditorPermission, UpdateAPIView):
    # Make sure Preview
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.preview = True
