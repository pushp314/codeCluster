from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['name', 'email', 'hackerrank_id', 'phone_number', 'college_name', 'transaction_id']
