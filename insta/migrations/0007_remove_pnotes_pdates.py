# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 02:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0006_pnotes_pdates'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pnotes',
            name='pdates',
        ),
    ]