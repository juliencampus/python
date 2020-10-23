from django.http import HttpResponse
from django.shortcuts import render
from cal.models import Event
from cal.forms import EventForm
import json


# Create your views here.
def index(request):
    events = Event.objects.all()
    events_list = []
    for event in events:
        e = {'id': event.id, 'title': event.title, 'description': event.description,
             'start': event.start.strftime("%Y-%m-%dT%H:%M"),
             'end': event.end.strftime("%Y-%m-%dT%H:%M"),
             'allday': event.allday,
             'url': f'http://127.0.0.1:8000/calendar/detail/{event.id}/'}
        events_list.append(e)
        print(json.dumps(events_list))
    context = {'format_events': json.dumps(events_list)}
    return render(request, 'cal/index.html', context)


def detail(request, event_id):
    event = Event.objects.get(pk=event_id)
    e = {'id': event.id, 'title': event.title, 'description': event.description,
         'start_day': event.start.strftime("%d / %m / %Y"),
         'start_time': event.start.strftime("%H : %M"),
         'end_day': event.end.strftime("%d / %m / %Y"),
         'end_time': event.end.strftime("%H : %M"),
         'allday': event.allday,
         }
    context = {'event_detail': e}
    return render(request, 'cal/detail.html', context)


def delete(request, event_id):
    Event.objects.filter(pk=event_id).delete()
    return index(request)


def create(request):
    form = EventForm()
    return render(request, 'cal/event_form.html', {'form': form})
    # print(request.POST)
    # string.join(request.PUT['start_time'])
    # print(string)

