# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parution',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 11, 6, 12, 14, 29, 570617, tzinfo=utc), verbose_name='Date de parution'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parution',
            name='titre',
            field=models.CharField(max_length=255, default='sans titre'),
        ),
    ]
