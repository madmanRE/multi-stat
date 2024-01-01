# Generated by Django 5.0 on 2024-01-01 11:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("socials", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="avatar",
            field=models.ImageField(
                default="profiles/profile/ava-default.png",
                null=True,
                upload_to="profiles/profile",
            ),
        ),
    ]