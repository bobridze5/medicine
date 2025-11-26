from django.urls import path
from . import views

app_name = 'profile'

urlpatterns = [
    path(
        # "<int:pk>/",
        '',
        views.DetailViewProfile.as_view(),
        name="profile_view"
    ),
    path(
        # '<int:pk>/edit/',
        'edit/',
        views.UpdateViewProfile.as_view(),
        name='profile_edit'
    ),

]
