# Generated by Django 3.0.3 on 2020-06-02 09:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20200602_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='updated_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 2, 14, 51, 20, 650223)),
        ),
        migrations.AlterField(
            model_name='sub_subject',
            name='sub_description',
            field=models.TextField(default=''),
        ),
    ]
