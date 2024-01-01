from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="профиль")
    username = models.CharField(max_length=100, default="-------")
    password = models.CharField(max_length=20, default="1111")
    phone = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="телефон"
    )
    email = models.EmailField(unique=True, verbose_name="электронная почта")
    avatar = models.ImageField(
        upload_to="profiles/profile",
        null=True,
        default="profiles/profile/ava-default.png",
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
