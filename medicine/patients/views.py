from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView, TemplateView
from .models import Patient, MedicalCard
from .forms import PatientForm
from django.urls import reverse_lazy


class PatientCreateView(CreateView):
    model = Patient
    form_class = PatientForm
    template_name = 'patient/patient_create_form.html'
    success_url = reverse_lazy('pages:homepage')

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)

        first_time = form.cleaned_data.get('first_time')
        card_number = form.cleaned_data.get('medical_record_number')

        if first_time:
            last_card = MedicalCard.objects.order_by('-id').first()
            if not last_card:
                available_number = 1
            else:
                available_number = int(last_card.number) + 1

            MedicalCard.objects.create(
                patient=self.object,
                number=str(available_number).zfill(6)
            )

        else:
            card = MedicalCard.objects.get(number=card_number)
            card.patient = self.object
            card.save()

        return response
