from django.db.models.functions import Lower
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView, CreateView)
from patients.models import MedicalCard, Patient
from doctors.models import Doctor, Specialization
from .models import Appointment, TimeSlot
from .forms import AppointmentForm


class SpecializationListView(LoginRequiredMixin, ListView):
    model = Specialization
    template_name = 'appointments/specialization_list.html'
    context_object_name = 'specializations'

    # TODO: присутствует проблема с буквой первой буквой
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q', '').strip()

        if query:
            search_term = query.lower()
            queryset = queryset.annotate(
                name_lower=Lower('name'),
                desc_lower=Lower('description')
            ).filter(
                Q(name_lower__icontains=search_term) |
                Q(desc_lower__icontains=search_term)
            )

        return queryset


class DoctorBySpecializationListView(LoginRequiredMixin, ListView):
    model = Doctor
    template_name = 'appointments/doctors_by_specialization.html'
    context_object_name = 'doctors'

    # TODO: присутствует проблема с буквой первой буквой
    def get_queryset(self):
        spec_id = self.kwargs['spec_id']
        queryset = Doctor.objects.filter(specialization_id=spec_id)

        query = self.request.GET.get('q', '').strip()

        if query:
            search_term = query.lower()
            queryset = queryset.filter(
                Q(user__settings__first_name__icontains=search_term) |
                Q(user__settings__last_name__icontains=search_term) |
                Q(user__settings__middle_name__icontains=search_term)
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['specialization'] = get_object_or_404(
            Specialization, id=self.kwargs['spec_id'])
        return context


class AppointmentCreateView(LoginRequiredMixin, CreateView):
    model = Appointment
    template_name = 'appointments/appointment_create.html'
    form_class = AppointmentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        doctor = get_object_or_404(Doctor, id=self.kwargs['doctor_id'])
        context['doctor'] = doctor

        selected_date = self.request.GET.get("date")
        context['selected_date'] = selected_date

        if selected_date:
            busy = Appointment.objects.filter(
                doctor=doctor,
                date=selected_date
            ).values_list("slot_id", flat=True)

            context['slots'] = TimeSlot.objects.exclude(id__in=busy)
        else:
            context['slots'] = None

        return context

    def form_valid(self, form):
        doctor = get_object_or_404(Doctor, id=self.kwargs['doctor_id'])
        user = self.request.user
        patient = get_object_or_404(Patient, user=user)

        slot_id = self.request.POST.get("slot")
        if not slot_id:
            form.add_error(None, "Выберите время приёма.")
            return self.form_invalid(form)

        # Проверяем занятость
        if Appointment.objects.filter(
            doctor=doctor,
            date=form.cleaned_data['date'],
            slot_id=slot_id
        ).exists():
            form.add_error(None, "Этот временной интервал уже занят.")
            return self.form_invalid(form)

        form.instance.slot_id = slot_id
        form.instance.doctor = doctor
        form.instance.patient = patient
        form.instance.medical_card = MedicalCard.objects.get(patient=patient)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('appointment:appointment_detail', kwargs={'pk': self.object.pk})


# -----------------------------------------------------------
# 4. Список всех записей пациента
# -----------------------------------------------------------
class PatientAppointmentsListView(LoginRequiredMixin, ListView):
    model = Appointment
    template_name = 'appointments/my_appointments.html'
    context_object_name = 'appointments'

    def get_queryset(self):
        patient = Patient.objects.get(user=self.request.user)
        return Appointment.objects.filter(patient=patient).order_by('-date',)


# -----------------------------------------------------------
# 5. Детальная информация о записи
# -----------------------------------------------------------
class AppointmentDetailView(LoginRequiredMixin, DetailView):
    model = Appointment
    template_name = 'appointments/appointment_detail.html'
    context_object_name = 'appointment'
