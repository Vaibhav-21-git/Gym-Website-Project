# Generated by Django 3.0.5 on 2020-07-13 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0060_auto_20200713_2033'),
        ('coaches', '0017_auto_20200713_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='presence_classes',
            field=models.ManyToManyField(blank=True, null=True, related_name='presence_classes', to='classes.Class'),
        ),
        migrations.AlterField(
            model_name='coach',
            name='private_classes',
            field=models.ManyToManyField(blank=True, null=True, related_name='private_classes', to='classes.PrivateOnlineClass'),
        ),
        migrations.AlterField(
            model_name='coach',
            name='public_classes',
            field=models.ManyToManyField(blank=True, null=True, related_name='public_classes', to='classes.PublicOnlineClass'),
        ),
    ]
