from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from . import forms
from django.views.generic import TemplateView,CreateView
from django.contrib.auth.forms import UserCreationForm 
from django.urls import reverse_lazy

# def index(request):
#   return render(request, "auto_mode/index.html",{})
# # Create your views here.

class TopView(TemplateView):
    template_name = "auto_mode/index.html"

class MyLoginView(LoginView):
    form_class = forms.LoginForm
    template_name = "accounts/login.html"

class MyLogoutView(LoginRequiredMixin, LogoutView):
    template_name = "accounts/logout.html"

class IndexView(TemplateView):
    template_name = "accounts/index.html"
    
class UserCreateView(CreateView):
    form_class = UserCreationForm
    template_name = "accounts/create.html"
    success_url = reverse_lazy("login")