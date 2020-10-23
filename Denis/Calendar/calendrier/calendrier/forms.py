from django.forms import ModelForm
from .models import Rdv

class RdvForm(ModelForm):
    class Meta:
        model = Rdv
        fields = ['heure', 'date', 'patient', 'types']

    def __init__(self, *args, **kwargs):
        super(RdvForm, self).__init__(*args, **kwargs)
        self.fields['heure'].widget.attrs.update({'class': 'form-group', 'disabled': 'disabled'})
        self.fields['date'].widget.attrs.update({'class': 'form-group', 'disabled': 'disabled'})
        self.fields['patient'].widget.attrs.update({'class': 'form-group', 'disabled': 'disabled'})