from django import forms

from . import models


class VehicleForm(forms.ModelForm):
    class Meta:
        model = models.Vehicle
        fields = ['vehicle_type', 'capacity', 'plaque']


class TravelForm(forms.ModelForm):
    class Meta:
        model = models.Travel
        fields = ['vehicle', 'datetime', 'origin', 'destination', 'is_two_way', 'price']


class BuyerForm(forms.ModelForm):
    class Meta:
        model = models.Buyer
        fields = ['buyer_name', 'buyer_phone', 'buyer_sex']


class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ['travel', 'buyer', 'seat_number']
