from django.db import models
from django.urls import reverse, reverse_lazy
import datetime


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
    def ends_at(self):
        return models.DateTimeField((self.starts_at + self.duration))

    def __str__(self):
        return f"{self.patient} : from {self.starts_at} to {self.ends_at.verbose_name} ({self.duration}')"

# Create your models here.
