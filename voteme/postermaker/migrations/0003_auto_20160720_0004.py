# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-19 15:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('postermaker', '0002_auto_20160708_1133'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('twitter_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('twitter_account', models.CharField(default='', max_length=30)),
                ('oauth_token', models.CharField(db_index=True, max_length=255, unique=True)),
                ('oauth_token_secret', models.CharField(db_index=True, max_length=255, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='politician',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postermaker.Politician'),
        ),
    ]
