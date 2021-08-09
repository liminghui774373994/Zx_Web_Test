from django.contrib import admin
from django.urls import re_path
from django.views.static import serve

from ZxWebTest import settings
from tools import views

urlpatterns = [
    re_path(r'^migrate/', views.test),

]
