from django.db import models
from django.urls import reverse, reverse_lazy
import datetime
import calendar


class Appointment(models.Model):
    APT_DURATIONS = (
        (datetime.timedelta(minutes=30), 'Normal'),
        (datetime.timedelta(minutes=45), 'Specialized'),
        (datetime.timedelta(minutes=55), 'Handling')
    )
    starts_at = models.DateTimeField()
    duration = models.DurationField(choices=APT_DURATIONS)
    patient = models.CharField(max_length=100)

    @property
    def get_html_url(self):
        url = "http://127.0.0.1:8000/calendar/"
        return f'<p>{self.patient}</p><a href="{url}">edit</a>'

    @property
    def ends_at(self):
        return models.DateTimeField((self.starts_at + self.duration))

    def __str__(self):
        return f"{self.patient} : from {self.starts_at} to {self.ends_at.verbose_name} ({self.duration}')"


# Create your models here.
