# coding=utf-8
from django.contrib import admin
from app01 import models


class BBS_admin(admin.ModelAdmin):
    # 一行展示多列
    list_display = ('title', 'summary', 'author', 'signature', 'view_count', 'created_at')
    # 按照创建时间过滤
    list_filter = ('created_at',)
    # 添加搜索
    search_fields = ('title', 'author__user__username')

    # 在BBS表中显示author表中的signature
    def signature(self, object):
        return object.author.signature


# Register your models here.
admin.site.register(models.BBS, BBS_admin)
admin.site.register(models.Category)
admin.site.register(models.BBS_user)