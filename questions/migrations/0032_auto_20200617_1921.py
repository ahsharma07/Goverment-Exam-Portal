# Generated by Django 3.0.6 on 2020-06-17 13:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0031_auto_20200617_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='updated_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 17, 19, 21, 42, 993562)),
        ),
    ]
