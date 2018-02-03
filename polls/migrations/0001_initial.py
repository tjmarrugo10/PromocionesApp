# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-03 21:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Promocion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=1000)),
                ('imagen', models.CharField(max_length=1000)),
                ('descripcion', models.CharField(max_length=1000)),
                ('valor', models.IntegerField(default=0)),
                ('fecha', models.DateTimeField()),
                ('categoria', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='polls.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=1000)),
                ('apellido', models.CharField(max_length=1000)),
                ('pais', models.CharField(max_length=1000)),
                ('ciudad', models.CharField(max_length=1000)),
                ('direccion', models.CharField(max_length=1000)),
                ('correo', models.CharField(max_length=1000)),
                ('categorias', models.ManyToManyField(to='polls.Categoria')),
            ],
        ),
        migrations.AddField(
            model_name='comentario',
            name='promocion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Promocion'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Usuario'),
        ),
    ]
