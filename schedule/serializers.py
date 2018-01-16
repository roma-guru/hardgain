from rest_framework import serializers
from .models import *


class ExerciseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'


class CycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cycle
        fields = '__all__'


class ScheduleDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleDay
        fields = '__all__'
