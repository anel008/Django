from .models import Booking
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class Bookingform(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            'booking_date' : DateInput(),
        }

        labels = {
            'p_name' : "patient name",
            'p_phone' : "patient phone number",
            'p_email': "patient email address",
            'doc_name' : "doctor name",
            'booking_date' : "booking date",
            'booked_on' : "booked on"
        }