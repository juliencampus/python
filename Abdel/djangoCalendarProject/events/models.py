# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse


class Event(models.Model):
    day = models.DateField(u'Jour événement', help_text=u'Jour événement')
    start_time = models.TimeField(u'Heure de départ', help_text=u'Heure de départ')
    end_time = models.TimeField(u'Heure de fin', help_text=u'Heure de fin')
    notes = models.TextField(u'Notes textuelles', help_text=u'Notes textuelles', blank=True, null=True)

    class Meta:
        verbose_name = u'R.D.V'
        verbose_name_plural = u'Planifications'

    def check_overlap(self, fixed_start, fixed_end, new_start, new_end):
        overlap = False
        if new_start == fixed_end or new_end == fixed_start:  # edge case
            overlap = False
        elif (fixed_start <= new_start <= fixed_end) or (
                fixed_start <= new_end <= fixed_end):  # innner limits
            overlap = True
        elif new_start <= fixed_start and new_end >= fixed_end:  # outter limits
            overlap = True

        return overlap

    def get_absolute_url(self):
        url = reverse('admin:%s_%s_change' % (self._meta.app_label, self._meta.model_name), args=[self.id])
        return u'<a href="%s">%s</a>' % (url, str(self.start_time))

    def clean(self):
        if self.end_time <= self.start_time:
            raise ValidationError('Les heures de fin doivent etre après les heures de début')

        events = Event.objects.filter(day=self.day)
        if events.exists():
            for event in events:
                if self.check_overlap(event.start_time, event.end_time, self.start_time, self.end_time):
                    raise ValidationError(
                        'Il y a chevauchement avec un autre événement: ' + str(event.day) + ', ' + str(
                            event.start_time) + '-' + str(event.end_time))
