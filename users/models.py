# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime

class User(models.Model):
    '''用户信息项'''
    nikename = models.CharField(max_length=64,unique=True)
    phonenum = models.CharField(max_length=16,unique=True)
    SEX = (
        ('男','男'),
        ('女','女'),
    )
    sex = models.CharField(choices=SEX,max_length=8)
    birth_year = models.IntegerField()
    birth_month = models.IntegerField()
    birth_day = models.IntegerField()
    avatar = models.CharField(max_length=256)
    location = models.CharField(max_length=32)

    @property
    def age(self):
        now = datetime.date.today()
        birth_date = datetime.date(self.birth_year,self.birth_month,self.birth_day)
        return (now - birth_date).days//365

class Profile(models.Model):
    '''用户配置项'''
    SEX = (
        ('男','男'),
        ('女','女'),
    )

    dating_sex = models.CharField(verbose_name='匹配性别',choices=SEX,max_length=8)
    location = models.CharField(verbose_name='目标城市',max_length=32)

    max_distance = models.IntegerField(verbose_name='最远距离',)
    min_distance = models.IntegerField(verbose_name='最近距离',)

    max_dating_age = models.IntegerField(verbose_name='最大年龄')
    mix_dating_age = models.IntegerField(verbose_name='最小年龄')

    vibration = models.BooleanField(default=True,verbose_name='是否开启震动')
    only_matche = models.Field(default=True,verbose_name='不让陌生人看我的相册')
    auto_play = models.BooleanField(default=True,verbose_name='自动播放视频')