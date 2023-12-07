from django.urls import path
from .views import *

urlpatterns = [
    path('slider/', SliderAPIView.as_view()),
    path('direction', DirectionApiView.as_view()),
    path('gallery/', GalleryApiView.as_view())
]
