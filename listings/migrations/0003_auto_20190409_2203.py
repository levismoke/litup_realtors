# Generated by Django 2.2 on 2019-04-09 19:03

import autoslug.fields
from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_listing_recommend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='body',
            field=tinymce.models.HTMLField(blank=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='description',
            field=tinymce.models.HTMLField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='listing',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True),
        ),
    ]
