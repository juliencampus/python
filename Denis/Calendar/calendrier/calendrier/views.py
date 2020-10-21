from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
import datetime

from .models import Rdv

# Create your views here.
def calendrier(request):

    rdv = [Rdv.objects.filter(date__day = date.today().day + i) for i in range(0, 7)]
    return render(request, 'calendrier/calendrier.html', {'rdv': rdv})