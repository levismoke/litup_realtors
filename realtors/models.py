from django.db import models
from autoslug import AutoSlugField
from datetime import datetime

# Create your models here.
class Realtor(models.Model):
    name = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='name')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    twitter = models.URLField(max_length=200, blank=True)
    instagram = models.URLField(max_length=200, blank=True)
    linkedin = models.URLField(max_length=200, blank=True)
    facebook = models.URLField(max_length=200, blank=True)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name