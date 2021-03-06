# Generated by Django 3.1.2 on 2020-10-21 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20201020_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='firstname',
            field=models.CharField(default='John', help_text='Indiquez votre prénom', max_length=100, verbose_name='Prénom'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='name',
            field=models.CharField(default='Doe', help_text='Indiquez votre nom', max_length=100, verbose_name='Nom'),
            preserve_default=False,
        ),
    ]
