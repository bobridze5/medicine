from django.contrib import admin
from .models import Appointment, TimeSlot

# Register your models here.
admin.site.register(TimeSlot)
admin.site.register(Appointment)
