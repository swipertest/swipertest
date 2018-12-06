# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-06 08:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dating_sex', models.CharField(choices=[('\u7537', '\u7537'), ('\u5973', '\u5973')], default='\u5973', max_length=8, verbose_name='\u5339\u914d\u6027\u522b')),
                ('location', models.CharField(max_length=32, verbose_name='\u76ee\u6807\u57ce\u5e02')),
                ('max_distance', models.IntegerField(default=10, verbose_name='\u6700\u8fdc\u8ddd\u79bb')),
                ('min_distance', models.IntegerField(default=1, verbose_name='\u6700\u8fd1\u8ddd\u79bb')),
                ('max_dating_age', models.IntegerField(default=40, verbose_name='\u6700\u5927\u5e74\u9f84')),
                ('mix_dating_age', models.IntegerField(default=18, verbose_name='\u6700\u5c0f\u5e74\u9f84')),
                ('vibration', models.BooleanField(default=True, verbose_name='\u662f\u5426\u5f00\u542f\u9707\u52a8')),
                ('only_matche', models.BooleanField(default=True, verbose_name='\u4e0d\u8ba9\u964c\u751f\u4eba\u770b\u6211\u7684\u76f8\u518c')),
                ('auto_play', models.BooleanField(default=True, verbose_name='\u81ea\u52a8\u64ad\u653e\u89c6\u9891')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=64, unique=True)),
                ('phonenum', models.CharField(max_length=16, unique=True)),
                ('sex', models.CharField(choices=[('\u7537', '\u7537'), ('\u5973', '\u5973')], max_length=8)),
                ('birth_year', models.IntegerField(default=2000)),
                ('birth_month', models.IntegerField(default=1)),
                ('birth_day', models.IntegerField(default=1)),
                ('avatar', models.CharField(max_length=256)),
                ('location', models.CharField(max_length=32)),
            ],
        ),
    ]
