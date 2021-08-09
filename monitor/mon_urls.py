from django.contrib import admin
from django.urls import re_path
from django.views.static import serve

from ZxWebTest import settings
from monitor import views

urlpatterns = [
    re_path(r'^newcms/', views.chains),
    re_path(r'^index/', views.view),
    #re_path(r'^crontab/', views.crontab),
    #re_path(r'^cms2_task_list/', views.cms2_task_list),
]
