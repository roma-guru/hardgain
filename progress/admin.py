from django.contrib import admin

from progress.models import *


@admin.register(TrainDay)
class TrainDayAdmin(admin.ModelAdmin):
    list_display = ('date', 'program', 'mood')
    list_filter = ('program', 'mood')
    ordering = ('date',)
    search_fields = ('date',)

@admin.register(TrainResult)
class TrainResultAdmin(admin.ModelAdmin):
    list_display = ('exercise', 'result', 'measure', 'day')
    list_editable = ('result',)
    list_filter = ('day', 'exercise')
    ordering = ('day__date',)
    autocomplete_fields = list_filter
