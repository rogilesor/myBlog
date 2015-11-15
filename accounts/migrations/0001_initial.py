# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', null=True, blank=True)),
                ('username', models.CharField(unique=True, max_length=255)),
                ('email', models.EmailField(verbose_name='email address', unique=True, max_length=255)),
                ('first_name', models.CharField(null=True, max_length=120, blank=True)),
                ('last_name', models.CharField(null=True, max_length=120, blank=True)),
                ('is_member', models.BooleanField(verbose_name='tout contenu', default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
