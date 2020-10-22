# Generated by Django 3.1.2 on 2020-10-22 08:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendrier', '0013_auto_20201022_1026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rdv',
            name='type',
        ),
        migrations.AddField(
            model_name='rdv',
            name='types',
            field=models.DurationField(choices=[(datetime.timedelta(seconds=1800), 'Simple'), (datetime.timedelta(seconds=3300), 'Manipulation'), (datetime.timedelta(seconds=2700), 'Spécialisé')], default=datetime.timedelta(seconds=1800)),
        ),
        migrations.AlterField(
            model_name='types',
            name='type',
            field=models.DurationField(choices=[(datetime.timedelta(seconds=1800), 'Simple'), (datetime.timedelta(seconds=3300), 'Manipulation'), (datetime.timedelta(seconds=2700), 'Spécialisé')]),
        ),
    ]
