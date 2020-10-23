from django.db import models
from django.contrib.auth.models import User
import datetime

class Horaires(models.Model):
    jourSemaine = models.IntegerField(default=0)
    ouverture = models.TimeField('ouverture')
    fermeture = models.TimeField('fermeture')

    def __str__(self):
        return str(self.jourSemaine)


class Rdv(models.Model):

    SIMPLE = 30
    SPECIALISE = 45
    MANIPULATION = 55


    CHOICES = {(SIMPLE, 'Simple'), (SPECIALISE, 'Spécialisé'), (MANIPULATION, 'Manipulation')}

    date = models.DateField('date')
    heure = models.TimeField('heure')
    types = models.IntegerField(choices=CHOICES, default=SIMPLE)
    patient = models.ForeignKey(User, on_delete=models.CASCADE)

    # def __str__(self):
        # return str(self.heure)

