# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-14 08:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sslproject', '0010_employee_current_institue'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='current_institue',
            new_name='currentinstitute',
        ),
    ]
