from django.forms import ModelForm
from .models import Rdv

class RdvForm(ModelForm):
     class Meta:
        model = Rdv
        fields = ['heure', 'date', 'types', 'patient']