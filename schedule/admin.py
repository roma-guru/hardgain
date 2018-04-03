from django.contrib import admin
from django.utils.html import format_html

from schedule.models import *


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_base', 'html_img', 'desc', 'html_a')
    list_filter = ('is_base',)
    search_fields = ('name', 'desc')

    def html_img(self, obj):
        return format_html(f"<img height='100px' src='{obj.image_link}'></img>")
    html_img.short_description = 'Image'

    def html_a(self, obj):
        return format_html(f"<a target='_blank' href='{obj.link}'>Ссылка</a>")
    html_a.short_description = 'Link'


@admin.register(Cycle)
class CycleAdmin(admin.ModelAdmin):
    list_display = ('name', 'active', 'start_date', 'end_date', 'completed')
    list_filter = ('active', 'completed')
    search_fields = ('name',)


@admin.register(DayProgram)
class DayProgram(admin.ModelAdmin):
    list_display = ('cycle', 'weekday')
    list_filter = list_display
    filter_horizontal = ('exercises',)
