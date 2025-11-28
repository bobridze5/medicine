from django.db import models
from doctors.models import Doctor
from patients.models import Patient, MedicalCard


class TimeSlot(models.Model):
    start = models.TimeField()
    end = models.TimeField()

    def __str__(self):
        return f"{self.start} - {self.end}"


class Appointment(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='appointments'
    )

    medical_card = models.ForeignKey(
        MedicalCard,
        on_delete=models.CASCADE,
        related_name='appointments'
    )

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name='appointments'
    )

    slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
    date = models.DateField('Дата')

    reason = models.TextField(
        blank=True,
        null=True,
        verbose_name="Причина обращения"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('doctor', 'date', 'slot')

    def __str__(self):
        return f"{self.date} {self.doctor}"
