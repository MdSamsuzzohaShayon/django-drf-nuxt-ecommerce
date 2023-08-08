from django.db import models
from PIL import Image
from django.core.files import File
from io import BytesIO
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.
def product_image_upload(instance, filename):
    return 'uploads/{filename}'.format(filename=filename)

def category_image_upload(instance, filename):
    return 'uploads/{filename}'.format(filename=filename)

def compress_image(image, quality):
    im = Image.open(image)
    if im.mode != 'RGB':
        im = im.convert('RGB')
    im_io = BytesIO()
    im.save(im_io, 'jpeg', quality=50,optimize=True)
    new_image = File(im_io, name=image.name)
    return new_image


class Category(MPTTModel):
    name = models.CharField(blank=False, null=False, unique=True, max_length=100)
    parent = TreeForeignKey(
        "self", null=True, blank=True, related_name="children", on_delete=models.SET_NULL
    )
    image = models.ImageField(upload_to=category_image_upload, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self,force_insert=False, force_update=False, using=None,*args, **kwargs):
        if self.image:
            image = self.image
            if image.size > 0.3*1024*1024: #if size greater than 300kb then it will send to compress image function
                self.image = compress_image(image=image, quality=50)
        super(Category, self).save(*args, **kwargs)


    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    title = models.CharField(blank=False, null=False, unique=True, max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=0, blank=False, null=False)
    discount_price = models.DecimalField(max_digits=10, decimal_places=0)
    # image_list = models.CharField # Make one to many relationship
    total_stock = models.DecimalField(max_digits=10, decimal_places=0)
    description = models.TextField()
    category = TreeForeignKey(
        Category, related_name="product_category", on_delete=models.SET_NULL, null=True, blank=True
    )
    image1 = models.ImageField(upload_to=product_image_upload, blank=True, null=True)
    image2 = models.ImageField(upload_to=product_image_upload, blank=True, null=True)
    image3 = models.ImageField(upload_to=product_image_upload, blank=True, null=True)
    image4 = models.ImageField(upload_to=product_image_upload, blank=True, null=True)
    # category = TreeForeignKey("Category", on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
    
# class Image

