# Generated by Django 3.0.6 on 2020-05-13 14:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0011_auto_20200513_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='class_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 5, 13, 19, 3, 29, 771014)),
        ),
    ]
