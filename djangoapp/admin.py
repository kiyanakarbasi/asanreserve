from django.contrib import admin
from . import models

for model in [models.Vehicle, models.Travel, models.Ticket]:
    admin.site.register(model)
