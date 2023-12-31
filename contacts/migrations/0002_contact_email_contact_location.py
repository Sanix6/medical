# Generated by Django 5.0 on 2023-12-07 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Электронный адрес'),
        ),
        migrations.AddField(
            model_name='contact',
            name='location',
            field=models.CharField(blank=True, max_length=55, null=True, verbose_name='Местоположение'),
        ),
    ]
