from django.shortcuts import render
from django.views import generic
from .models import Appointment
from .utils import Calendar
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
import calendar
import datetime


class IndexView(generic.ListView):
    model = Appointment
    template_name = 'appointments/index.html'
    success_url = reverse_lazy("index")

    # def get_queryset(self):
    #     """Returns Appointments this week"""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)

        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.date.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - datetime.timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + datetime.timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month
      # date = datetime.date.today()
        # start_week = date - datetime.datetime.timedelta(date.weekday())
        # end_week = start_week + datetime.datetime.timedelta(7)
        # return Appointment.objects.filter(starts_at__range=[start_week, end_week])
# Create your views here.
