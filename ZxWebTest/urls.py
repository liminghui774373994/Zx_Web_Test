"""ZxWebTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.templatetags import static
from django.urls import path
from django.conf.urls import include,re_path
from django.views.static import serve

from ZxWebTest import settings


urlpatterns = [
    # re_path(r'^static/(?P<path>.*)$', serve,
    #     {'document_root': settings.STATIC_ROOT}, name='static'),
    path('admin/', admin.site.urls),
    re_path(r'^user/', include(('myxmind.myxmind_urls', 'login'))),
    re_path(r'^leap/', include(('leap.leap_urls', 'leap'))),
    re_path(r'^myxmind/', include(('myxmind.myxmind_urls', 'myxmind'))),
    re_path(r'^tools/', include(('tools.tools_urls', 'migrate'))),
    re_path(r'^mon/', include(('monitor.mon_urls', 'index'))),
    re_path(r'^data/', include(('mta.mta_urls'))),


]
