# Generated by Django 3.1.7 on 2021-05-01 01:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0002_auto_20210418_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtuber',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 1, 10, 55, 30, 720571)),
        ),
    ]
