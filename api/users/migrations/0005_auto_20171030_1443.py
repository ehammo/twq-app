# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-30 14:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_employee'),
        ('users', '0004_auto_20171030_1426'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
