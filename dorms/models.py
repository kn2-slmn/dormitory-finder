from django.db import models
from accounts.models import OwnerProfile

# Create your models here.

class Dormitory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # location = 
    owner = models.OneToOneField(OwnerProfile, on_delete=models.CASCADE)
    rent = models.CharField(max_length=20)
    rules = models.TextField()
    # requirements
    amenities = models.TextField()
    approved = models.BooleanField(default=False)
    slug = models.SlugField(unique=True) 

    class Meta:
        verbose_name_plural = 'dormitories'