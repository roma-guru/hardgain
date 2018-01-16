from rest_framework import serializers
from .models import *


class TrainDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainDay
        fields = '__all__'


class TrainResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainResult
        fields = '__all__'
