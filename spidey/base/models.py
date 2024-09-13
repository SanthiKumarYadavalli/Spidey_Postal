from django.db import models

# Create your models here.
class Stamp(models.Model):
    image_url = models.CharField(max_length=500)
    postal_circle = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    
class Order(models.Model):
    stamp = models.ForeignKey(Stamp)
    status = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 