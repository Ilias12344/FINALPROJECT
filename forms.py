from django import forms
from .models import PainRecord

class PainRecordForm(forms.ModelForm):
    class Meta:
        model = PainRecord
        fields = ['severity', 'duration', 'location', 'pain_type', 'trigger']
