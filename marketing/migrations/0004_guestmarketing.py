# Generated by Django 3.0.5 on 2020-07-05 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0003_auto_20200705_1711'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuestMarketing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guest_email', models.EmailField(max_length=254)),
            ],
        ),
    ]
