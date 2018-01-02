from django.db import models
from datetime import date

class Exercise(models.Model):
    """
    Basic Exercise info: name, description, link to sportswiki,
    and is it base exercise (most important).
    """
    name:str = models.CharField(max_length=255)
    desc:str = models.CharField(max_length=255)
    link:str = models.CharField(max_length=255, blank=True)
    is_base:bool = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Cycle(models.Model):
    """
    Training cycle of progressing.
    It is dates interval when I'm able to increase weights.
    """
    name:str = models.CharField(max_length=255, blank=True, default='')
    start_date:date = models.DateField()
    end_date:date = models.DateField(null=True)
    comment:str = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

class ScheduleDay(models.Model):
    """
    Weekday microtraining program - includes weekday and
    scheduled exercises. Linked to Cycle.
    """
    WEEKDAYS = (
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
        ('Sun', 'Sunday'),
    )
    weekday = models.CharField(max_length=15, choices=WEEKDAYS)
    comment = models.CharField(max_length=255, blank=True)
    cycle = models.ForeignKey(Cycle, on_delete=models.CASCADE, related_name='schedule')
    exercises = models.ManyToManyField(Exercise)

    def __str__(self):
        return f"{self.cycle}: {self.weekday}"
