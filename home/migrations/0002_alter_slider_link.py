# Generated by Django 5.0 on 2023-12-07 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка'),
        ),
    ]
