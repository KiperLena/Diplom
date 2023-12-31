from django.forms import ModelForm
from django import forms
from .models import Report, Bid


class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = ['field', 'title', 'type', 'description', 'name']
        widgets = {
            'name': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-report'})

class BidForm(ModelForm):
    class Meta:
        model = Bid
        fields = ['title', 'area', 'field', 'type', 'purpose', 'number', 'name', 'important', 'user_bid', 'phone', 'user']
        widgets = {
            'name': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-report'})


