from rest_framework import serializers
from .models import *


class ContSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cont
        fields = '__all__'


class DoctorSerializers(serializers.ModelSerializer):
    cat = ContSerializers(read_only=True)

    class Meta:
        model = Doctor
        fields = [
            'image',
            'full_name',
            'direction',
            'experience',
            'cat'
        ]


class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = [
            'image',
            'title',
            'subtitle'
        ]
