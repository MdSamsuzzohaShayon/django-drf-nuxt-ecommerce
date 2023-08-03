# Generated by Django 4.2.3 on 2023-08-02 16:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_alter_user_first_name_alter_user_last_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "country",
                    models.CharField(
                        blank=True, default="Bangladesh", max_length=100, null=True
                    ),
                ),
                ("city", models.CharField(max_length=100)),
                ("phone_number", models.IntegerField(blank=True, null=True)),
                ("area", models.CharField(max_length=255)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="address",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
