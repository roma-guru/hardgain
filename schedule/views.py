from rest_framework import viewsets, views, response, status, permissions
from django.db.models import Max
from datetime import datetime
from logging import getLogger
log = getLogger(__name__)

from .models import *
from progress.models import *
from .serializers import *


class ExerciseViewSet(viewsets.ModelViewSet):
    """ Exercises CRUD. """
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class CycleViewSet(viewsets.ModelViewSet):
    """ Cycles CRUD. """
    queryset = Cycle.objects.all()
    serializer_class = CycleSerializer


class ScheduleDayViewSet(viewsets.ModelViewSet):
    """ ScheduleDays CRUD. """
    queryset = ScheduleDay.objects.all()
    serializer_class = ScheduleDaySerializer


class DayView(views.APIView):
    """
    Today's program view on frontend.
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, day=None, format=None):
        """ Get React app state. """
        log.info(f"Requesting program for {day}")
        today = datetime.strptime(day, '%Y-%m-%d').date()
        cycle = Cycle.objects.get(active=True,
                                  start_date__lt=today, end_date__gt=today)
        log.debug(f"cycle={cycle}")

        try:
            sched = ScheduleDay.objects.get(
                cycle=cycle, weekday=today.weekday())
            log.debug(f"sched={sched}")
            program = []
            # Get exercises list with max weights
            for ex in sched.exercises.all():
                best_res = TrainResult.objects.filter(exercise=ex,
                                                      day__program__cycle=cycle).aggregate(Max('result'))
                ex_serialized = ExerciseSerializer(ex,
                                                   context={'request': request}).data
                ex_serialized['result'] = best_res['result__max']
                program.append(ex_serialized)
        except ScheduleDay.DoesNotExist:
            # Relax today
            log.info("Have nothing to do today!")
            program = None

        # Return final json
        resp = {'today': today,
                'cycle': CycleSerializer(cycle).data,
                'program': program,
                }
        return response.Response(resp)
