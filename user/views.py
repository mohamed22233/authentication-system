from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms

# Create your views here.
class Register(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("user:login")
    template_name = "user/register.html"

