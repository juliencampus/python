from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'cal'

urlpatterns = [
    path('', views.CalendarView.as_view(), name='calendar'),
    # url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
]
