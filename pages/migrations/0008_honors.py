# Generated by Django 3.0.5 on 2020-07-16 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_auto_20200715_1636'),
    ]

    operations = [
        migrations.CreateModel(
            name='Honors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='honors/%Y/%m/%d')),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'افتخارت باشگاه',
            },
        ),
    ]