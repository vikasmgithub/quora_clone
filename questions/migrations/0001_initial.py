# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 13:58
from __future__ import unicode_literals

import autoslug.fields
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
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('content', models.CharField(blank=True, max_length=500, null=True)),
                ('tag', models.IntegerField(choices=[(0, 'Sports'), (5, 'Entertainment'), (10, 'Science'), (15, 'Politics'), (20, 'Environment')])),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from=models.CharField(max_length=80), unique=True)),
                ('asked_at', models.DateTimeField(auto_now_add=True)),
                ('edited_at', models.DateTimeField(auto_now=True)),
                ('asked_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
