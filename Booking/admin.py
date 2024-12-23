from django.contrib import admin
from .models import Passenger,Flight
# Register your models here.

models =[ Passenger,Flight]

for model in models:
    admin.site.register(model)