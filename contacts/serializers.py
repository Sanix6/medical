from rest_framework import serializers
from .models import *


class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['numbers', 'location', 'email']
