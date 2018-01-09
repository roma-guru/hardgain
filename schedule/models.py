from django.db import models
from datetime import date

class Exercise(models.Model):
    """
    Basic Exercise info: name, description, link to sportswiki,
    and is it base exercise (most important).
    """
    name:str = models.CharField(max_length=255)
    desc:str = models.CharField(max_length=255, blank=True)
    sets:str = models.CharField(max_length=255, blank=True)
    image_link:str = models.CharField(max_length=1000, blank=True)
    link:str = models.CharField(max_length=255, blank=True)
    comment:str = models.TextField(blank=True)
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
    comment:str = models.TextField(blank=True)
    active:bool = models.BooleanField(default=True)
    completed:bool = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class ScheduleDay(models.Model):
    """
    Weekday microtraining program - includes weekday and
    scheduled exercises. Linked to Cycle.
    """
    WEEKDAYS = (
        (0, 'Понедельник'),
        (1, 'Вторник'),
        (2, 'Среда'),
        (3, 'Четверг'),
        (4, 'Пятница'),
        (5, 'Суббота'),
        (6, 'Воскресение'),
    )
    _weekdays_dict = dict(WEEKDAYS)
    weekday = models.SmallIntegerField(choices=WEEKDAYS)
    cycle = models.ForeignKey(Cycle, on_delete=models.CASCADE, related_name='schedule')
    exercises = models.ManyToManyField(Exercise)
    comment:str = models.TextField(blank=True)

    def __str__(self):
        return f"{self.cycle}: {self._weekdays_dict[self.weekday]}"
