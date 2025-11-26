from django.contrib.auth import get_user_model
from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import ProfileForm

User = get_user_model()


class UpdateViewProfile(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileForm
    template_name = 'profile/profile_form.html'
    success_url = reverse_lazy('pages:homepage')

    def get_object(self):
        return self.request.user

# TODO: надо убрать отображение у других пользователей


class DetailViewProfile(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'profile/profile_detail.html'

    def get_object(self):
        return self.request.user
