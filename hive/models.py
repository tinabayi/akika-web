from django.db import models

# Create your models here.

class Product(models.Model):
    product_image = models.ImageField(upload_to = 'image/')
    product_name = models.CharField(max_length =30)
    description = models.TextField()
   
