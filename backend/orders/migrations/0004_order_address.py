# Generated by Django 4.2.3 on 2023-08-03 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
        ("orders", "0003_remove_order_shipping_address"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="address",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="shipping_address",
                to="accounts.address",
            ),
            preserve_default=False,
        ),
    ]
