# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 02:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='images',
            field=models.ImageField(upload_to='issue_images'),
        ),
    ]
