# Generated by Django 3.1.2 on 2020-10-20 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendrier', '0004_auto_20201020_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horaires',
            name='fermeture',
            field=models.TimeField(verbose_name='fermeture'),
        ),
    ]
