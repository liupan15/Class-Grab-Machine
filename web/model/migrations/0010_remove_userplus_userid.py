# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-20 03:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0009_userplus_userid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userplus',
            name='userid',
        ),
    ]
