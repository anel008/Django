from .models import Booking
from django import forms

class Bookingform(forms.ModelForm):
    class meta:
        model = Booking
        fields = '__all__'