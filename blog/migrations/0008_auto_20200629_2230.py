# Generated by Django 3.0.1 on 2020-06-29 21:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200629_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 29, 22, 30, 32, 626984)),
        ),
        migrations.AlterField(
            model_name='post',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 29, 22, 30, 32, 625987)),
        ),
    ]
