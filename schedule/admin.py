from django.contrib import admin
from django.utils.html import format_html

from schedule.models import *

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('html_img', 'is_base', 'name', 'desc', 'html_a')

    def html_img(self, obj):
        return format_html(f"<img height='100px' src='{obj.image_link}'></img>")
    html_img.short_description = 'Image'

    def html_a(self, obj):
        return format_html(f"<a target='_blank' href='{obj.link}'>Link</a>")
    html_a.short_description = 'Link'

@admin.register(Cycle)
class CycleAdmin(admin.ModelAdmin):
    list_display = ('name', 'active', 'start_date', 'end_date', 'completed')

@admin.register(ScheduleDay)
class ScheduleDay(admin.ModelAdmin):
    list_display = ('cycle', 'weekday')
