# Generated by Django 3.0.6 on 2020-05-25 08:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0045_auto_20200514_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='class_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 5, 25, 13, 8, 55, 667729)),
        ),
    ]
