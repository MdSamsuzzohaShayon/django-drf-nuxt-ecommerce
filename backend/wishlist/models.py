from django.db import models

# Create your models here.
class Wishlist(models.Model):
    email = models.CharField(max_length=100, blank=False, null=False)
    preview = models.BooleanField(default=False)

