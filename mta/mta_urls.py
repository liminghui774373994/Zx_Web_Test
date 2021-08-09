from django.urls import re_path
from django.views.static import serve

from ZxWebTest import settings
from mta import views

urlpatterns = [
    re_path(r'^mta/', views.mta_add),
    re_path(r'^mtalist/', views.mta_list),
    re_path(r'^mtacheck/', views.check_data)
]