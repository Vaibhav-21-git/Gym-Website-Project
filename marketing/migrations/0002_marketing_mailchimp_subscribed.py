# Generated by Django 3.0.5 on 2020-07-04 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='marketing',
            name='mailchimp_subscribed',
            field=models.NullBooleanField(),
        ),
    ]
