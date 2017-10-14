# coding=utf-8
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# 创建表


# 帖子表
class BBS(models.Model):
    category = models.ForeignKey('Category')
    title = models.CharField(max_length=64)  # 帖子标题，标题可以重复
    summary = models.CharField(max_length=256, blank=True, null=True)  # 帖子介绍
    content = models.TextField()  # 评论
    author = models.ForeignKey('BBS_user')  # 作者
    view_count = models.IntegerField()  # 浏览数
    ranking = models.IntegerField()  # 排名
    created_at = models.DateTimeField(auto_now_add=True)  # 创建日期,自动添加
    updated_at = models.DateTimeField(auto_now_add=True)  # 修改日期

    def __unicode__(self):
        return self.title


# 模块表 版主
class Category(models.Model):
    name = models.CharField(max_length=32, unique=True)  # 板块名称
    administrator = models.ForeignKey('BBS_user')  # 版主

    def __unicode__(self):
        return self.name


# BBS用户表
class BBS_user(models.Model):
    user = models.OneToOneField(User)  # 一对一的外键
    signature = models.CharField(max_length=128, default='This guy is too lazy to leave anything here')  # 个性签名
    photo = models.ImageField(upload_to="upload_imgs/", default="upload_imgs/user1.jpg")  # 头像图片

    def __unicode__(self):
        return self.user.username