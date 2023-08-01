from django.forms import ModelForm
from django import forms
from .models import Report


class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = ['field', 'title', 'type', 'description', 'name']
        widgets = {
            'type': forms.CheckboxSelectMultiple(),
            'name': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-report'})







