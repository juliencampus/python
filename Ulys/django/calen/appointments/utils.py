from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Appointment


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    def formatday(self, day, appointments):
        appointments_per_day = appointments.filter(starts_at__day=day)
        d = ''
        for apt in appointments_per_day:
            d += f'<li class="calendar_list"> {apt.get_html_url} </li>'
        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
        return '<td></td>'

    def formatweek(self, theweek, appointments):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, appointments)
        return f'<tr> {week} </tr>'

    def formatmonth(self, withyear=True):
        appointments = Appointment.objects.filter(starts_at__year=self.year, starts_at__month=self.month)
        cal = f'<table border="0" cellpadding="0" cellspacing="0"     class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, appointments)}\n'
        return cal