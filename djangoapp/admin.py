from django.contrib import admin
from . import models

for model in [item for item in dir(models) if not item.startswith('__') and item != 'models']:
    admin.site.register(eval(f'models.{model}'))
