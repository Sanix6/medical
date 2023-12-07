from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *


class ContactApiView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializers
