from django.urls import path
from . import views

app_name = 'patients'

urlpatterns = [
    path(
        'create/',
        views.PatientCreateView.as_view(),
        name='patient_create'
    ),
]
