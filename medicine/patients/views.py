from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView, TemplateView
from .models import Patient
from .forms import PatientForm
from django.urls import reverse_lazy
# Create your views here.


class PatientCreateView(CreateView):
    model = Patient
    form_class = PatientForm
    template_name = 'patient/patient_create_form.html'
    success_url = reverse_lazy('pages:homepage')
