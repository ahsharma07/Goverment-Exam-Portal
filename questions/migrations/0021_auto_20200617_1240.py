# Generated by Django 2.2.7 on 2020-06-17 12:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0020_auto_20200617_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='updated_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 17, 12, 40, 19, 906846)),
        ),
    ]
