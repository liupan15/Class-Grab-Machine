# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-19 10:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0006_remove_lesson_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='time',
        ),
    ]