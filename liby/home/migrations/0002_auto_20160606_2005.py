# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-06 23:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Troca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota_1', models.IntegerField()),
                ('nota_2', models.IntegerField()),
                ('avaliacao_1', models.TextField()),
                ('avaliacao_2', models.TextField()),
                ('concluida', models.BooleanField(default=False)),
                ('data', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='transacao',
            name='livro',
        ),
        migrations.RemoveField(
            model_name='transacao',
            name='usuarioSolicitante',
        ),
        migrations.RemoveField(
            model_name='mensagem',
            name='destinatario',
        ),
        migrations.RemoveField(
            model_name='mensagem',
            name='transacao',
        ),
        migrations.AlterField(
            model_name='livro',
            name='dono',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='livros', to='home.Perfil'),
        ),
        migrations.AlterField(
            model_name='mensagem',
            name='remetente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensagens', to='home.Perfil'),
        ),
        migrations.DeleteModel(
            name='Transacao',
        ),
        migrations.AddField(
            model_name='troca',
            name='livro_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Livro'),
        ),
        migrations.AddField(
            model_name='troca',
            name='livro_2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='livros_trocados', to='home.Livro'),
        ),
        migrations.AddField(
            model_name='troca',
            name='perfil_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Perfil'),
        ),
        migrations.AddField(
            model_name='troca',
            name='perfil_2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trocas', to='home.Perfil'),
        ),
        migrations.AddField(
            model_name='mensagem',
            name='troca',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.Troca'),
            preserve_default=False,
        ),
    ]
