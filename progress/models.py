from django.db import models
from schedule.models import *
from datetime import date

class TrainDay(models.Model):
    program:ScheduleDay = models.ForeignKey(ScheduleDay, null=True, on_delete=models.SET_NULL)
    date:date = models.DateField()
    comment:str = models.CharField(max_length=255)
    mood:str = models.CharField(max_length=1)

class TrainResult(models.Model):
    day:TrainDay = models.ForeignKey(TrainDay, on_delete=models.CASCADE)
    exercise:Exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    result:float = models.FloatField()
    measure:str = models.CharField(max_length=5, default='kg')
    comment:str = models.CharField(max_length=255, blank=True)
