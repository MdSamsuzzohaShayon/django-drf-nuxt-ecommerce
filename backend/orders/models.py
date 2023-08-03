from django.db import models
from accounts.models import Address, User
from products.models import Product

# Create your models here.
    # product = models.ForeignKey( Product, related_name="product_orders", on_delete=models.CASCADE)
    # quantity = models.IntegerField()

class Order(models.Model):
    PENDING = "PG"
    SHIPPING = "SG"
    COMPLETED = "CD"

    STATUS_CHOICES = [
        (PENDING, "PENDING"),
        (SHIPPING, "SHIPPING"),
        (COMPLETED, "COMPLETED")
    ]

    status = models.CharField( max_length=2, choices=STATUS_CHOICES, default=PENDING)
    is_paid = models.BooleanField(default=False)
    buyer = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="order_product", on_delete=models.CASCADE)
    address = models.ForeignKey(Address, related_name="shipping_address", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total = models.IntegerField() # Price * Quantity
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)