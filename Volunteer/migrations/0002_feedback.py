# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-02 16:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ngo', '0004_auto_20180317_1336'),
        ('Volunteer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(max_length=250)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ngo.Event')),
            ],
        ),
    ]