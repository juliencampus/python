# Generated by Django 3.1.2 on 2020-10-22 08:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendrier', '0012_auto_20201021_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rdv',
            name='type',
            field=models.DurationField(choices=[(datetime.timedelta(seconds=3300), 'Manipulation'), (datetime.timedelta(seconds=1800), 'Simple'), (datetime.timedelta(seconds=2700), 'Spécialisé')]),
        ),
        migrations.AlterField(
            model_name='types',
            name='type',
            field=models.DurationField(choices=[(datetime.timedelta(seconds=3300), 'Manipulation'), (datetime.timedelta(seconds=1800), 'Simple'), (datetime.timedelta(seconds=2700), 'Spécialisé')]),
        ),
    ]
