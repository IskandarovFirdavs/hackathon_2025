from django import forms
from .models import Booking, Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'age', 'contact']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['patient', 'doctor', 'date', 'time', 'notes']
