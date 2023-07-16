# Generated by Django 4.2.3 on 2023-07-16 18:59

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_rename_image_url_category_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to=products.models.upload_to
            ),
        ),
    ]
