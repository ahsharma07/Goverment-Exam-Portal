# Generated by Django 2.2.7 on 2020-06-17 12:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0016_auto_20200617_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='updated_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 17, 12, 29, 3, 24728)),
        ),
    ]