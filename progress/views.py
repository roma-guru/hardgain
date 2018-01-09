from django.shortcuts import render
from rest_framework import viewsets

from .models import *
from .serializers import *


class TrainDayViewSet(viewsets.ModelViewSet):
    queryset = TrainDay.objects.all()
    serializer_class = TrainDaySerializer

class TrainResultViewSet(viewsets.ModelViewSet):
    queryset = TrainResult.objects.all()
    serializer_class = TrainResultSerializer

