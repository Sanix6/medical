from django.urls import path
from .views import *

urlpatterns = [
    path('med/', DoctorApiView.as_view()),
    path('news/', NewsApiView.as_view())
]
