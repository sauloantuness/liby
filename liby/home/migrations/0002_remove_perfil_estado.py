# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-25 11:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='estado',
        ),
    ]
