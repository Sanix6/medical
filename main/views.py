from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *


class DoctorApiView(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializers


class NewsApiView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers