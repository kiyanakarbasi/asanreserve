from django.db import models


class Vehicle(models.Model):
    vehicle_type = models.CharField(max_length=100)
    capacity     = models.IntegerField()
    plaque       = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.vehicle_type=} - {self.plaque=}'


class Travel(models.Model):
    vehicle      = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    datetime     = models.DateTimeField()
    origin       = models.CharField(max_length=100)
    destination  = models.CharField(max_length=100)
    is_two_way   = models.BooleanField(default=False)
    price        = models.IntegerField()

    def __str__(self):
        return f'{self.vehicle=} - {self.price=}'


class Buyer(models.Model):
    buyer_name   = models.CharField(max_length=100)
    buyer_phone  = models.CharField(max_length=20, unique=True)
    buyer_sex    = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.buyer_name=}'


class Ticket(models.Model):
    travel       = models.ForeignKey(Travel, on_delete=models.CASCADE)
    buyer        = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    seat_number  = models.IntegerField()

    def __str__(self):
        return f'{self.seat_number=} - {self.buyer=} - {self.travel=}'
