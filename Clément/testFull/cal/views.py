from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
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
             'url': f'/calendar/event/{event.id}/'}
        events_list.append(e)
    context = {'format_events': json.dumps(events_list)}
    return render(request, 'cal/index.html', context)



def event_form(request, event_id=False):
    if not event_id:
        if request.method == 'GET':
            form = EventForm()
            return render(request, 'cal/event_form.html', {'form': form, 'creation': True})
        else:
            f = EventForm(request.POST)
            f.save()
            return index(request)
    else:
        event = Event.objects.get(pk=event_id)
        if request.method == 'GET':
            form = EventForm(initial={'title': event.title, 'description': event.description, 'start': event.start, 'end': event.end}).is_valid()
            return render(request, 'cal/event_form.html', {'form': form, 'creation': False})
        else:
            instance = get_object_or_404(Event, id=event_id)
            f = EventForm(request.POST, instance=instance).is_valid()
            if request.POST.get("update"):
                f.save()
            elif request.POST.get("delete"):
                event.delete()
            return index(request)
