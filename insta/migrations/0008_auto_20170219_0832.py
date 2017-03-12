# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 03:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0007_remove_pnotes_pdates'),
    ]

    operations = [
        migrations.AddField(
            model_name='pnotes',
            name='pdate',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='pnotes',
            name='pmonth',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='pnotes',
            name='pyear',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pnotes',
            name='pnotes',
            field=models.TextField(null=True),
        ),
    ]