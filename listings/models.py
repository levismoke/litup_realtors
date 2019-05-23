from django.db import models
from autoslug import AutoSlugField
from datetime import datetime
from realtors.models import Realtor
from categories.models import Category
from cats.models import Cat

# Create your models here.
class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    cat = models.ForeignKey(Cat, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True)
    address = models.CharField(max_length=200)
    town = models.CharField(max_length=200)
    county = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    description = models.TextField(max_length=500, blank=True)
    body = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=5, decimal_places=1)
    garage = models.IntegerField()
    sqft = models.IntegerField()
    stories = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=2)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    recommend = models.BooleanField(default=False)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title