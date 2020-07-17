# Generated by Django 3.0.6 on 2020-05-14 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0004_banner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banner',
            options={'verbose_name_plural': 'Banner'},
        ),
        migrations.AddField(
            model_name='coach',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
    ]