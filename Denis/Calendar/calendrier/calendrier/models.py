from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Types(models.Model):

    SIMPLE = datetime.timedelta(minutes=30)
    SPECIALISE = datetime.timedelta(minutes=45)
    MANIPULATION = datetime.timedelta(minutes=55)


    CHOICES = {(SIMPLE, 'Simple'), (SPECIALISE, 'Spécialisé'), (MANIPULATION, 'Manipulation')}
    type = models.DurationField(choices=CHOICES)

    def __str__(self):
        return str(self.type)

class Horaires(models.Model):
    jourSemaine = models.IntegerField(default=0)
    ouverture = models.TimeField('ouverture')
    fermeture = models.TimeField('fermeture')

    def __str__(self):
        return str(self.jourSemaine)


class Rdv(models.Model):
    date = models.DateField('date')
    heure = models.TimeField('heure')
    type = models.ForeignKey(Types, on_delete=models.CASCADE)
    patient = models.ForeignKey(User, on_delete=models.CASCADE)

    # def __str__(self):
        # return str(self.heure)

