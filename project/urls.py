"""
URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers

from schedule.views import *
from progress.views import *


router = routers.DefaultRouter()

# Schedule app
router.register(r'exercises', ExerciseViewSet)
router.register(r'cycles', CycleViewSet)
router.register(r'program', DayProgramViewSet)

# Progress app
router.register(r'trainings', TrainDayViewSet)
router.register(r'results', TrainResultViewSet)

# URL Patterns
urlpatterns = [
    url(r'^api/day/(?P<day>\d{4}-\d{2}-\d{2})$',
        DayView.as_view()),
    url(r'^api/day/(?P<day>\d{4}-\d{2}-\d{2})/complete_exercise$',
        CompleteExerciseView.as_view()),
    url(r'^api/', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('django.contrib.auth.urls')),
    url(r'^rest-auth/', include('djoser.urls')),
    url(r'^rest-auth/', include('djoser.urls.jwt')),
]
