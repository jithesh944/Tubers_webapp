# Generated by Django 3.1.7 on 2021-06-13 06:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0004_auto_20210613_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtuber',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 13, 15, 19, 29, 932967)),
        ),
    ]
