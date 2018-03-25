from django.shortcuts import render
from rest_framework import authentication, permissions, viewsets, views, response

from schedule.models import * 
from progress.models import *
from progress.serializers import *


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
    permission_classes = (permissions.AllowAny,)

    def post(self, request, day=None, format=None):
        log.info("Completed exercise")
        log.debug(f"Request body: {request.body}")
        req_json = json.loads(request.body)
        # TODO: return 400
        assert "weight" in req_json and "id" in req_json,\
                "Required fields"
        ex_id = int(req_json['id'])
        weight = float(request['weight'])
        log.info(f"Exercise {ex_id} with result {weight}")

        # 1. Determine current cycle
        today = datetime.strptime(day, '%Y-%m-%d').date()
        log.debug(f"Parsed date is {today}")
        cycle = Cycle.objects.get(active=True,
                                  start_date__lt=today,
                                  end_date__gt=today)
        log.debug(f"Found cycle: {cycle}")
        # 2. Determine day program
        program = ScheduleDay.objects.get(cycle=cycle,
                                weekday=today.weekday())
        log.debug(f"Found sched day: {program}")
        # 3. Get/create train day object
        day = TrainDay.get_or_create(program=program,
                                     date=today)
        log.debug(f"Get/Create train day: {day}")
        # 4 Find exercise
        exercise = Exercise.objects.get(pk=ex_id)
        # 5. Create train result
        tr = TrainResult(day, exercise, weight)
        log.info(f"Created train result: {tr}")
        return response.Response()
