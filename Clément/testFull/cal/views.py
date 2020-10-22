from django.http import HttpResponse
from django.shortcuts import render
from cal.models import Event
import json


# Create your views here.
def index(request):
    events = Event.objects.all()
    events_list = []
    for event in events:
        e = {'id': event.id, 'title': event.title, 'description': event.description,
             'start': event.start.strftime("%Y-%m-%dT%H:%M:%S"),
             'end': event.end.strftime("%Y-%m-%dT%H:%M:%S"), 'allday': event.allday, 'url': f'http://127.0.0.1:8000/calendar/detail/{event.id}/'}
        events_list.append(e)
    print(events_list)
    context = {'format_events': json.dumps(events_list)}
    return render(request, 'cal/index.html', context)


def detail(request, event_id):
    print('why')
    return render(request, 'cal/detail.html')
