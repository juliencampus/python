# Generated by Django 3.1.2 on 2020-10-20 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendrier', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horaires',
            name='fermeture',
            field=models.TimeField(verbose_name='fermture'),
        ),
        migrations.AlterField(
            model_name='horaires',
            name='ouverture',
            field=models.TimeField(verbose_name='ouverture'),
        ),
    ]