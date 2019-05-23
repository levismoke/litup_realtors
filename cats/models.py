from django.db import models
from autoslug import AutoSlugField

# Create your models here.
class Cat(models.Model):
    name = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='name')
    def __str__(self):
        return self.name