from rest_framework import serializers
from .models import *


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ['title', 'subtitle', 'img', 'link', 'is_activate']


class DirectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Direction
        fields = ['image', 'title']


class GallerySerializer(serializers.ModelSerializer):

    class Meta:
        model = Gallery
        fields = ['image']


class GalleryPreviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ('id', 'image', 'year')


class YearGallerySerializer(serializers.Serializer):
    year = serializers.IntegerField()
    images = GalleryPreviewSerializer(many=True)
