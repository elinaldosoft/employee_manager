# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-17 19:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=200, unique=True, verbose_name='nome'),
        ),
    ]