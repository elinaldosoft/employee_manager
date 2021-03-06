# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-17 19:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_auto_20170617_1642'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='nome')),
                ('description', models.TextField(null=True)),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
                'db_table': 'departaments',
                'ordering': ('-created_at',),
            },
        ),
        migrations.AlterField(
            model_name='employee',
            name='departament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_departament_set', to='employees.Departament'),
        ),
    ]
