from django.urls import path
from . import views

app_name = 'appointment'

urlpatterns = [
    # 1. Список специализаций
    path(
        'specializations/',
        views.SpecializationListView.as_view(),
        name='specialization_list'
    ),

    # 2. Список врачей по специализации
    path(
        'specializations/<int:spec_id>/doctors/',
        views.DoctorBySpecializationListView.as_view(),
        name='doctors_by_specialization'
    ),

    # 3. Выбор времени и создание записи
    path(
        'doctor/<int:doctor_id>/create/',
        views.AppointmentCreateView.as_view(),
        name='appointment_create'
    ),

    # 4. Список всех записей пациента
    path(
        'my/', views.PatientAppointmentsListView.as_view(),
        name='my_appointments'
    ),

    # 5. Детальная информация о записи (по желанию)
    path(
        '<int:pk>/', views.AppointmentDetailView.as_view(),
        name='appointment_detail'
    ),

    path(
        '<int:pk>/delete/',
        views.AppointmentDeleteView.as_view(),
        name='appointment_delete'
    ),



]
