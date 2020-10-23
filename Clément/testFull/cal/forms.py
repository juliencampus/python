from django.forms import ModelForm, forms
from .models import Event


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'start', 'end']

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['start'].widget.attrs.update({'class': 'form-control'})
        self.fields['end'].widget.attrs.update({'class': 'form-control'})
        # self.fields['allday'].widget.attrs.update({'class': 'form-check-input', 'type': 'checkbox', 'style': 'margin-left:10px'})

        error_messages = {
            'application': {
                'required': ("Application field is required"),
            },
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start")
        end_date = cleaned_data.get("end")

        if start_date and end_date and end_date < start_date:
            raise forms.ValidationError(
                    "end_date should be greater than start_date."
                )