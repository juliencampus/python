from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
import datetime
from django.utils.safestring import mark_safe
from django.utils.datastructures import MultiValueDictKeyError

from .forms import RdvForm
from .models import Rdv

def findIndex(heure):
    heureTotal = heure.hour * 60 + heure.minute
    return round((heureTotal - (8 * 60)) /15)

def changeCreneau(rdv):

    creneaux = [(datetime.datetime(hour=8, day=1, minute=0, year=2020, month=4) + datetime.timedelta(minutes= i * 15), mark_safe('<a href='+'/rdv/'+str(i)+'/'+str(date.today() + datetime.timedelta(days=i))+'>Prendre RDV</a>'), 'blue') for i in range(0, 41)]

    for el in rdv:
        totalTemps = round(el.types / 15)
        for i in range(0, totalTemps):
            creneaux[findIndex(el.heure) + i] = (datetime.datetime(hour=el.heure.hour, day=1, minute=0, year=2020, month=4) + datetime.timedelta(minutes= i * 15), el.patient, 'red')

    return creneaux

# Create your views here.
def calendrier(request):

    days = {date.today() + datetime.timedelta(days=i): changeCreneau(Rdv.objects.filter(date__day = date.today().day + i)) for i in range(0, 7)}
    return render(request, 'calendrier/calendrier.html', {'days': days})

def takerdv(request, idHeure, date):
    idHeure = (8 * 60) + (idHeure * 15)
    heure = round(idHeure / 60)
    minute = round(idHeure - (heure * 60))

    if minute < 10:
        minute = '0'+str(minute)
    else:
        minute = str(minute)

    if heure < 10:
        heure = '0'+str(heure)
    else:
        heure = str(heure)

    heureTotal = heure+':'+minute

    userId = request.user.id

    form = RdvForm(initial={'date': date, 'heure': heureTotal, 'patient': userId})

    return render(request, 'calendrier/takerdv.html', {'form': form})

def saveRdv(request):
    f = RdvForm(request.POST)
    if f.is_valid():
        f.save()
    else:
        f.save()

    return HttpResponse("Saaaaave")