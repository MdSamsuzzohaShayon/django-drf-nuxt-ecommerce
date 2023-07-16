from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.

class Category(MPTTModel):
    name = models.CharField(blank=False, null=False, unique=True, max_length=100)
    parent = TreeForeignKey(
        "self", null=True, blank=True, related_name="children", on_delete=models.SET_NULL
    )
    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    title = models.CharField(blank=False, null=False, unique=True, max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=0, blank=False, null=False)
    discount_price = models.DecimalField(max_digits=10, decimal_places=0)
    # image_list = models.CharField # Make one to many relationship
    total_stock = models.DecimalField(max_digits=10, decimal_places=0)
    desc = models.TextField()
    category = TreeForeignKey(
        Category, related_name="product_category", on_delete=models.SET_NULL, null=True, blank=True
    )
    # category = TreeForeignKey("Category", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return self.title
    
# class Image

