# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-10 20:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='catergory',
            new_name='category',
        ),
    ]
