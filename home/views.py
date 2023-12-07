from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

class SliderAPIView(generics.ListAPIView):
    serializer_class = SliderSerializer

    def get_queryset(self):
        queryset = Slider.objects.filter(is_active=True)
        sorted_queryset = sorted(queryset, key=lambda obj: obj.id)
        return sorted_queryset


class DirectionApiView(generics.ListAPIView):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer


class GalleryApiView(generics.ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer

    def list(self, request, *args, **kwargs):
        year = request.query_params.get('year')

        if not year.isnumeric():
            return Response(data={'message': 'Year must be a valid number!'}, status=status.HTTP_404_NOT_FOUND)

        images = Gallery.objects.filter(year=year)
        serializer = self.get_serializer(images, many=True)

        if not images.exists():
            return Response(data={'message': 'Не найден!'}, status=status.HTTP_404_NOT_FOUND)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class GalleryPreviewListAPIView(ListAPIView):
    serializer_class = YearGallerySerializer

    def get_queryset(self):
        years = Gallery.objects.values_list('year', flat=True).distinct().order_by('year')
        queryset = []

        for year in years:
            gallery_objects = Gallery.objects.filter(year=year)[:4]
            year_gallery_data = {
                'year': year,
                'images': gallery_objects
            }
            queryset.append(year_gallery_data)

        return queryset

