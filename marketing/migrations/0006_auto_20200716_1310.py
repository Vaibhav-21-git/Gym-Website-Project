# Generated by Django 3.0.5 on 2020-07-16 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0005_auto_20200705_1750'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='guestmarketing',
            options={'verbose_name_plural': 'ایمیل های بازاریابی مهمانان'},
        ),
        migrations.AlterModelOptions(
            name='marketing',
            options={'verbose_name_plural': 'ایمیل های بازاریابی کاربران'},
        ),
    ]
