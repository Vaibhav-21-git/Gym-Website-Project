# Generated by Django 3.0.5 on 2020-07-16 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0006_auto_20200715_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='is_guest',
            field=models.BooleanField(default=False),
        ),
    ]
