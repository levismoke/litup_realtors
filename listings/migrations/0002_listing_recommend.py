# Generated by Django 2.2 on 2019-04-08 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='recommend',
            field=models.BooleanField(default=False),
        ),
    ]
