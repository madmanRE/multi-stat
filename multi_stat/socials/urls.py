from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

app_name = "socials"

urlpatterns = [
    path(
        "login/",
        LoginView.as_view(template_name="socials/login.html"),
        name="login",
    ),
    path("logout/", LogoutView.as_view(next_page="main:index"), name="logout"),
]
