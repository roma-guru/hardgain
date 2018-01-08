from django.db import models
from schedule.models import *
from datetime import date

class TrainDay(models.Model):
    program:ScheduleDay = models.ForeignKey(ScheduleDay, null=True, on_delete=models.SET_NULL)
    date:date = models.DateField()
    mood:str = models.CharField(max_length=5)
    comment:str = models.TextField(blank=True)

    def __str__(self):
        return f"{self.date} {self.mood} [ {self.program} ]"

class TrainResult(models.Model):
    day:TrainDay = models.ForeignKey(TrainDay, on_delete=models.CASCADE)
    exercise:Exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    result:float = models.FloatField()
    measure:str = models.CharField(max_length=5, default='кг')
    comment:str = models.TextField(blank=True)

    def __str__(self):
        return f"{self.exercise} - {self.result} {self.measure} [ {self.day} ]"
