from django.contrib.auth import get_user_model
from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from .forms import ProfileForm
from .models import UserSettings
# User = get_user_model()


class ProfileChooseRoleView(LoginRequiredMixin, TemplateView):
    template_name = 'profile/profile_choose_role.html'


class CreateViewProfile(LoginRequiredMixin, CreateView):
    model = UserSettings
    form_class = ProfileForm
    template_name = 'profile/profile_create_form.html'
    success_url = reverse_lazy('profile:profile_choose_role')

    # def get_initial(self):
    #     return {'email': self.request.user.email}

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs['require_email'] = False
        return kwargs


class UpdateViewProfile(LoginRequiredMixin, UpdateView):
    model = UserSettings
    form_class = ProfileForm
    template_name = 'profile/profile_edit_form.html'
    success_url = reverse_lazy('profile:profile_view')

    def get_object(self):
        return UserSettings.objects.get(user=self.request.user)

    def get_initial(self):
        initial = super().get_initial()
        initial['email'] = self.request.user.email
        return initial

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs['require_email'] = True
        return kwargs

    def form_valid(self, form):
        response = super().form_valid(form)

        user = self.request.user
        user.email = form.cleaned_data['email']
        user.save()

        return response

# TODO: надо убрать отображение у других пользователей


class DetailViewProfile(LoginRequiredMixin, DetailView):
    model = UserSettings
    template_name = 'profile/profile_detail.html'

    def get_object(self):
        return UserSettings.objects.get(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = self.get_object()
        return context
