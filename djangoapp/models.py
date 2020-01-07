from django.db import models


class Vehicle(models.Model):
    vehicle_type = models.CharField(max_length=100)
    capacity     = models.IntegerField()
    plaque       = models.CharField(max_length=100)


class Travel(models.Model):
    vehicle      = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    datetime     = models.modelsDateTimeField()
    origin       = models.CharField(max_length=100)
    destination  = models.CharField(max_length=100)
    is_two_way   = models.BooleanField(default=False)
    price        = models.IntegerField()


class Buyer(models.Model):
    buyer_name   = models.CharField(max_length=100)
    buyer_phone  = models.CharField(max_length=20, unique=True)
    buyer_sex    = models.CharField(max_length=10)


class Tickets(models.Model):
    travel       = Models.ForeignKey(Travel, on_delete=models.CASCADE)
    buyer        = Models.ForeignKey(Buyer, on_delete=models.CASCADE)
    seat_number  = models.IntegerField()
