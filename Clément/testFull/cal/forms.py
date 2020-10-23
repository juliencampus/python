from django.forms import ModelForm, forms
from .models import Event


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'start', 'end', 'allday']

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['start'].widget.attrs.update({'class': 'form-control'})
        self.fields['end'].widget.attrs.update({'class': 'form-control'})
        self.fields['allday'].widget.attrs.update({'class': 'form-check-input', 'type': 'checkbox'})
