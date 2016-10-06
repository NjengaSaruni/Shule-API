# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-27 10:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_regist', models.DateField()),
                ('comment', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('number', models.CharField(default='1000', max_length=128)),
                ('students', models.ManyToManyField(through='darasa.Registration', to='darasa.Student')),
            ],
        ),
        migrations.AddField(
            model_name='registration',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='darasa.Student'),
        ),
        migrations.AddField(
            model_name='registration',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='darasa.Subject'),
        ),
    ]
