# Generated by Django 3.0.6 on 2020-05-13 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0003_auto_20200512_1826'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='banners/%Y/%m/%d')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
    ]
