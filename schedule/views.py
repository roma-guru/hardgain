from rest_framework import viewsets, views, response, status, permissions
from django.db.models import Max
from datetime import datetime
from logging import getLogger
log = getLogger(__name__)

from .models import *
from progress.models import *
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


class TodayView(views.APIView):
    """
    Class View for today's schedule.
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, format=None):
        log.info("Requesting Today Program")
        today = datetime.today()
        log.debug(f"today={today}")
        # TODO: add time interval check?
        cycle = Cycle.objects.get(active=True)
        log.debug(f"cycle={cycle}")

        try:
            sched = ScheduleDay.objects.get(cycle=cycle, weekday=today.weekday())
            log.debug(f"sched={sched}")
            program = []
            # Get exercises list with max weights
            for ex in sched.exercises.all():
                best_res = TrainResult.objects.filter(exercise=ex,
                        day__program__cycle=cycle).aggregate(Max('result'))
                program.append({'name': ex.name,
                    'pic': ex.image_link, 'last': best_res['result__max']})
        except ScheduleDay.DoesNotExist:
            # Relax today
            log.info("Have nothing to do today!")
            program = None

        resp = {'today': today,
                'cycle': CycleSerializer(cycle).data,
                'program': program,
                }
        return response.Response(resp)
