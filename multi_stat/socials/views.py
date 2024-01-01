from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegisterForm, ProfileForm
from .models import Profile
from django.db import IntegrityError
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView


def register(request):
    if request.method == "POST":
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            try:
                username = user_form.cleaned_data["username"]
                password = user_form.cleaned_data["password"]
                user = User.objects.create_user(username=username)
                user.set_password(password)
                user.save()
                login(request, user)
                profile = Profile.objects.create(
                    user=user,
                    username=username,
                    password=password,
                    phone=user_form.cleaned_data["phone"],
                    email=user_form.cleaned_data["email"],
                )
                profile.save()
                return redirect("/")
            except IntegrityError:
                form.add_error("login", "Пользователь с таким логином уже существует")
    else:
        user_form = RegisterForm()
    return render(request, "socials/register.html", {"user_form": user_form})


class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileForm
    success_url = "/"


class ProfileView(DetailView):
    template_name = "socials/profile.html"
    model = Profile
    context_object_name = "profile"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.object
        context["profile"] = profile
        return context
