from django import forms
from . models import RescueReport

class RescueReportForm(forms.ModelForm):
    class Meta:
        model = RescueReport
        fields = ['location', 'description', 'photo']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
