# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parution',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('auteur', models.CharField(max_length=100)),
                ('contenu', models.TextField(default='blabla')),
            ],
        ),
        migrations.CreateModel(
            name='TypeParution',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('type_parution', models.CharField(max_length=120)),
            ],
        ),
        migrations.AddField(
            model_name='parution',
            name='classement',
            field=models.ForeignKey(to='blog2.TypeParution'),
        ),
    ]
