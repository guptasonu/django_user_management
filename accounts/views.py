from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView

from accounts.forms import ProfileForm, SignUpForm


# Sign Up View
class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "commons/signup.html"


# Edit Profile View
class ProfileView(UpdateView):
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy("home")
    template_name = "commons/profile.html"


class UserListView(ListView):
    model = User
    template_name = "index.html"


class UserDetailsView(DetailView):
    model = User
    template_name = "commons/details.html"
