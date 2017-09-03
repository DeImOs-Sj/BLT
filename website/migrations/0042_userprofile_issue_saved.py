# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-02 14:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0041_auto_20170817_0202'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='issue_saved',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='saved', to='website.Issue'),
        ),
    ]