# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-16 23:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(default='No description', max_length=1000)),
                ('place', models.CharField(default='Raipur', max_length=50)),
                ('contact', models.IntegerField(max_length=10)),
                ('users', models.CharField(blank=True, max_length=1000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
