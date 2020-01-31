from django import forms

from . import models


class VehicleForm(forms.ModelForm):
    class Meta:
        model = models.Vehicle
        fields = ['vehicle_type', 'capacity', 'plaque', 'admin']


class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ['travel', 'seat_number', 'buyer_name', 'buyer_phone', 'buyer_sex']
