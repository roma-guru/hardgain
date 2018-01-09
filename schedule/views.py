from django.shortcuts import render
from rest_framework import viewsets

from .models import *
from .serializers import *


class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

class CycleViewSet(viewsets.ModelViewSet):
    queryset = Cycle.objects.all()
    serializer_class = CycleSerializer

class ScheduleDayViewSet(viewsets.ModelViewSet):
    queryset = ScheduleDay.objects.all()
    serializer_class = ScheduleDaySerializer

