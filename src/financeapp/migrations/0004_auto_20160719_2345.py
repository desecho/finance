# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-20 03:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financeapp', '0003_rename_models'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expense',
            options={'ordering': ['date']},
        ),
        migrations.AddField(
            model_name='category',
            name='essential',
            field=models.BooleanField(default=False),
        ),
    ]
