# Generated by Django 3.0.1 on 2020-06-29 12:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_auto_20200618_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 29, 13, 34, 49, 691525)),
        ),
    ]
