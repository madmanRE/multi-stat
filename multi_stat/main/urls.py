from django.urls import path
from .views import index, contacts, about

app_name = "main"

urlpatterns = [
    path("contacts/", contacts, name="contacts"),
    path("about-us/", about, name="about"),
    path("", index, name="index"),
]
