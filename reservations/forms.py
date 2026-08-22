from django import forms


class ReservationForm(forms.Form):
    date = forms.DateField(label="Select Date")
    time = forms.TimeField(label="Select Time")
