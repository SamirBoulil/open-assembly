# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-21 20:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('open_assembly', '0003_poll_is_solemn'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='deputy',
        ),
    ]