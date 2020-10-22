# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse

# Create your models here.


class Appointment(models.Model):
    SIMPLE = 'SIM'
    SPECIALISTE = 'SPE'
    MANIPULATION = 'MAN'
    APPOINTMENT_TYPE_CHOICES = [
        (SIMPLE, 'Rendez-vous simple'),
        (SPECIALISTE, 'Rendez-vous spécialiste'),
        (MANIPULATION, 'Rendez-vous avec manipulation'),
    ]

    name = models.CharField(u'Nom', help_text=u'Indiquez votre nom', max_length=100)
    firstname = models.CharField(u'Prénom', help_text=u'Indiquez votre prénom', max_length=100)
    day = models.DateField(u'Date', help_text=u'Sélectionnez une date')
    start_time = models.TimeField(u'Heure de début', help_text=u'Sélectionnez un heure de début')
    appointment_type = models.CharField(
        u'Type de rendez-vous',
        max_length=3,
        choices=APPOINTMENT_TYPE_CHOICES,
        default=SIMPLE,
        help_text=u'Sélectionnez un type de rendez-vous'
    )

    def get_absolute_url(self):
        url = reverse('admin:%s_%s_change' % (self._meta.app_label, self._meta.model_name), args=[self.id])
        return u'<a href="%s">%s</a>' % (url, str(self.start_time))

    # def check_overlap(self, fixed_start, fixed_end, new_start, new_end):
    #     overlap = False
    #     if new_start == fixed_end or new_end == fixed_start:  # edge case
    #         overlap = False
    #     elif (fixed_start <= new_start <= fixed_end) or (
    #             fixed_start <= new_end <= fixed_end):  # innner limits
    #         overlap = True
    #     elif new_start <= fixed_start and new_end >= fixed_end:  # outter limits
    #         overlap = True
    #     return overlap
    #
    # def clean(self):
    #     if self.end_time <= self.start_time:
    #         raise ValidationError('Ending times must after starting times')
    #
    #     events = Appointment.objects.filter(day=self.day)
    #     if events.exists():
    #         for event in events:
    #             if self.check_overlap(event.start_time, event.end_time, self.start_time, self.end_time):
    #                 raise ValidationError(
    #                     'There is an overlap with another event: ' + str(event.day) + ', ' + str(
    #                         event.start_time) + '-' + str(event.end_time))

