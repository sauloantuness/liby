# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-25 15:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_perfil_estado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=100)),
                ('capa', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('dono', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Perfil')),
            ],
        ),
    ]
