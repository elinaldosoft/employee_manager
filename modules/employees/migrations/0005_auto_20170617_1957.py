# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-17 22:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0004_auto_20170617_1953'),
    ]

    operations = [
        migrations.RenameField(
            model_name='departament',
            old_name='quantity',
            new_name='count_employee',
        ),
    ]
