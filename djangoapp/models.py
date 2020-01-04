from django.db import models


class Vehicle(models.Model):
    vehicle_type = models.CharField(max_length=40)
    capacity = models.
    Plaque = models.CharField(max_length=40)


class Travel(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    
