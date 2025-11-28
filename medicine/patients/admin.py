from django.contrib import admin
from .models import Patient, MedicalCard
# Register your models here.

admin.site.register(MedicalCard)
admin.site.register(Patient)
