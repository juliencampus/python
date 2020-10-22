from django.urls import path
from . import views
urlpatterns = [
    path('calendar/', views.index, name='index'),
    path(f'calendar/detail/<int:event_id>/', views.detail, name='detail'),
]
