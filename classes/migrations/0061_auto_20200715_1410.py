# Generated by Django 3.0.5 on 2020-07-15 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0060_auto_20200713_2033'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Banner',
        ),
        migrations.AlterModelOptions(
            name='class',
            options={'verbose_name_plural': 'کلاس های حضوری'},
        ),
    ]
