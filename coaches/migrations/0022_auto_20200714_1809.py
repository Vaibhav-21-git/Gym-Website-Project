# Generated by Django 3.0.5 on 2020-07-14 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0021_coach_live_stream_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coach',
            name='presence_classes',
        ),
        migrations.RemoveField(
            model_name='coach',
            name='private_classes',
        ),
        migrations.RemoveField(
            model_name='coach',
            name='public_classes',
        ),
    ]