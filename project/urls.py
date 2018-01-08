"""URL Configuration

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
from rest_framework import routers, viewsets

from schedule.models import *
from schedule.serializers import *
from progress.models import *
from progress.serializers import *

### DRF Viewsets
class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

class CycleViewSet(viewsets.ModelViewSet):
    queryset = Cycle.objects.all()
    serializer_class = CycleSerializer

class ScheduleDayViewSet(viewsets.ModelViewSet):
    queryset = ScheduleDay.objects.all()
    serializer_class = ScheduleDaySerializer

class TrainDayViewSet(viewsets.ModelViewSet):
    queryset = TrainDay.objects.all()
    serializer_class = TrainDaySerializer

class TrainResultViewSet(viewsets.ModelViewSet):
    queryset = TrainResult.objects.all()
    serializer_class = TrainResultSerializer


### DRF Routers
router = routers.DefaultRouter()

# Schedule app
router.register(r'exercises', ExerciseViewSet)
router.register(r'cycles', CycleViewSet)
router.register(r'schedule', ScheduleDayViewSet)

# Progress app
router.register(r'trainings', TrainDayViewSet)
router.register(r'results', TrainResultViewSet)


### URL Patterns
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
]
