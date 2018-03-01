from django.shortcuts import render
from rest_framework import viewsets, views, response

from .models import *
from .serializers import *


class TrainDayViewSet(viewsets.ModelViewSet):
    """ CRUD for TrainDays. """
    queryset = TrainDay.objects.all()
    serializer_class = TrainDaySerializer


class TrainResultViewSet(viewsets.ModelViewSet):
    """ CRUD for TrainResults. """
    queryset = TrainResult.objects.all()
    serializer_class = TrainResultSerializer

class CompleteExerciseView(views.APIView):
    """ Complete exercise endpoint for frontend. """
    def post(self, request, day=None, format=None):
        log.info(f"Completed exercise")
        return response.Response()
