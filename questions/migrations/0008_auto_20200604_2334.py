# Generated by Django 3.0.6 on 2020-06-04 18:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0007_auto_20200604_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='updated_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 4, 23, 34, 27, 147999)),
        ),
    ]
