from django.urls import path
from . import views
urlpatterns = [
    path('calendar/', views.index, name='index'),
    path(f'calendar/event/<int:event_id>/', views.event_form, name='form_detail'),
    path(f'calendar/detail/<int:event_id>/delete', views.delete, name='delete'),
    path(f'calendar/event/', views.event_form, name='form'),
]
