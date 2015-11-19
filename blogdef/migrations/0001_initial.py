# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parution',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('titre', models.CharField(default='sans titre', max_length=255)),
                ('auteur', models.CharField(max_length=100)),
                ('contenu', models.TextField(default='blabla')),
                ('date', models.DateTimeField(verbose_name='Date de parution', auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TypeParution',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('type_parution', models.CharField(max_length=120)),
            ],
        ),
        migrations.AddField(
            model_name='parution',
            name='classement',
            field=models.ForeignKey(to='blogdef.TypeParution'),
        ),
    ]
