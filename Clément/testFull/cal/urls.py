from django.urls import path
from . import views
urlpatterns = [
    path(f'', views.index, name='index'),
    path(f'calendar/', views.index, name='index'),
    path(f'calendar/event/<int:event_id>/', views.event_form, name='form_detail'),
    path(f'calendar/event/', views.event_form, name='form'),
]
