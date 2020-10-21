from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Appointment
import logging


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None, week=None):
        self.year = year
        self.month = month
        self.week = week
        super(Calendar, self).__init__()

    def formatday(self, day):
        appointments_per_day = Appointment.objects.filter(starts_at__day=day)
        d = ''
        for apt in appointments_per_day:
            d += f'<li class="calendar_list"> {apt.get_html_url} </li>'
        cell = f"<td><span class='date'></span><ul> {d} </ul></td>"
        return cell

    def formatweek(self):
        cal = f'<table border="0" cellpadding="0" cellspacing="0"     class="calendar">\n'
        cal += f'{self.formatweekheader()}\n'
        week = ''
        for theweek in self.monthdays2calendar(self.year, self.month):
            if datetime.today().strftime("%d") in [item[0] for item in theweek]:
                logging.warning(theweek)
                for d, weekday in theweek:
                    week += self.formatday(d)
                cal += f'<tr> {week} </tr>'
        return cal

# def formatmonth(self, withyear=True):
#     appointments = Appointment.objects.filter(starts_at__year=self.year, starts_at__month=self.month)
#     cal = f'<table border="0" cellpadding="0" cellspacing="0"     class="calendar">\n'
#     cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
#     cal += f'{self.formatweekheader()}\n'
#     for week in self.monthdays2calendar(self.year, self.month):
#         cal += f'{self.formatweek(week, appointments)}\n'
#     return cal
