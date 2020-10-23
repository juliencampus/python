from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import date
import datetime
from django.utils.safestring import mark_safe
import math
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate, login

from django.contrib import admin
from .forms import RdvForm
from .models import Rdv

def findIndex(heure):
    heureTotal = heure.hour * 60 + heure.minute
    return round((heureTotal - (8 * 60)) /15)

def changeCreneau(rdv, jour):

    creneaux = [(datetime.datetime(hour=8, day=1, minute=0, year=2020, month=4) + datetime.timedelta(minutes= i * 15), mark_safe('<a href='+'/rdv/'+str(i)+'/'+str(jour)+'>Prendre RDV</a>'), '') for i in range(0, 41)]

    for el in rdv:
        totalTemps = round(el.types / 15)
        for i in range(0, totalTemps):
            try:
                creneaux[findIndex(el.heure) + i] = (datetime.datetime(hour=el.heure.hour, day=1, minute=0, year=2020, month=4) + datetime.timedelta(minutes= i * 15), el.patient, 'bg-secondary')
            except:
                break

    return creneaux

# Create your views here.
def calendrier(request, jour=date.today().strftime('%Y-%m-%d')):
    if request.user.id is not None:

        days = {datetime.datetime.strptime(jour, '%Y-%m-%d') + datetime.timedelta(days=i): changeCreneau(Rdv.objects.filter(date__day = datetime.datetime.strptime(jour, '%Y-%m-%d').day + i, date__month = datetime.datetime.strptime(jour, '%Y-%m-%d').month), datetime.datetime.strptime(jour, '%Y-%m-%d') + datetime.timedelta(days=i)) for i in range(0, 7)}
        before = datetime.datetime.strptime(jour, '%Y-%m-%d') - datetime.timedelta(days=7)
        after = datetime.datetime.strptime(jour, '%Y-%m-%d') + datetime.timedelta(days=7)
        return render(request, 'calendrier/calendrier.html', {'days': days, 'before': before, 'after': after})
    else:
        return redirect('admin/login/?next=/admin/')


def takerdv(request, idHeure, date):
    minuteTotal = (8 * 60) + (idHeure * 15)
    heure = math.floor(minuteTotal / 60)
    minute = minuteTotal - (heure * 60)

    if minute < 10:
        minute = '0'+str(minute)
    else:
        minute = str(minute)

    if heure < 10:
        heure = '0'+str(heure)
    else:
        heure = str(heure)

    heureTotal = heure+':'+minute+':00'

    userId = request.user.id
    user = request.user

    form = RdvForm(initial={'date': date, 'heure': heureTotal, 'patient': userId})

    return render(request, 'calendrier/takerdv.html', {'form': form, 'user': user})

def saveRdv(request):
    f = RdvForm(request.POST)
    date = request.POST.get('date')
    heure = '2020-10-20 '+request.POST.get('heure')
    heureTotal = datetime.datetime.strptime(heure, '%Y-%m-%d %H:%M:%S') + datetime.timedelta(minutes=int(request.POST.get('types')))

    heuresRdv = Rdv.objects.filter(date__day = datetime.datetime.strptime(date, '%Y-%m-%d').day)

    isEmpty = True

    type(heure)
    type(date)

    for el in heuresRdv:
        heureRdv = datetime.datetime.strptime(date, '%Y-%m-%d') + datetime.timedelta(hours=el.heure.hour, minutes=el.heure.minute)
        if heureTotal > heureRdv:
            isEmpty = False
            break


    if isEmpty:
        f.save()
    else:
        return HttpResponse("C'est déja prit !")

    return redirect('../'+date)