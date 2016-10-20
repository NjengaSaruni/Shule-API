# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-07 07:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('darasa', '0005_auto_20161002_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='students', to=settings.AUTH_USER_MODEL),
        ),
    ]
