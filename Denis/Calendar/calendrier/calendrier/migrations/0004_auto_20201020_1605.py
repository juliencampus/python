# Generated by Django 3.1.2 on 2020-10-20 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendrier', '0003_remove_rdv_heure'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='types',
            name='manip',
        ),
        migrations.RemoveField(
            model_name='types',
            name='simple',
        ),
        migrations.RemoveField(
            model_name='types',
            name='special',
        ),
        migrations.AddField(
            model_name='types',
            name='type',
            field=models.IntegerField(default=30),
        ),
    ]
