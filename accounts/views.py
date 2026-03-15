from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .forms import CustomUserCreationForm

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/register.html'

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'
