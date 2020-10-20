# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

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

    day = models.DateField(u'Date', help_text=u'Sélectionnez une date')
    start_time = models.TimeField(u'Heure de début', help_text=u'Sélectionnez un heure de début')
    appointment_type = models.CharField(
        u'Type de rendez-vous',
        max_length=3,
        choices=APPOINTMENT_TYPE_CHOICES,
        default=SIMPLE,
        help_text=u'Sélectionnez un type de rendez-vous'
    )
