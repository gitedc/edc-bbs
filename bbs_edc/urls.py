# coding=utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
from app01 import views
import app01.urls

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'bbs_project.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       # 配置url
    url(r'^admin/', include(admin.site.urls)),

                       # 登陆页面url
    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    (r'^login/$', views.Login),
    (r'^acc_login/$', views.acc_login),
    (r'^logout/$', views.logout_view),

    url(r'', include(app01.urls)),
)
