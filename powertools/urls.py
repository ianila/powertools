"""powertools URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from controlpanel import views as controlpanel_views

urlpatterns = [
    url(r'^controlpanel/login/', controlpanel_views.controlpanel_login, name='controlpanel_login'),
    url(r'^controlpanel/logout/', controlpanel_views.controlpanel_logout, name='controlpanel_logout'),
    url(r'^controlpanel/home/', controlpanel_views.controlpanel_home, name='controlpanel_home'),
    url(r'^controlpanel/tools/', controlpanel_views.controlpanel_tools, name='controlpanel_tools'),
    url(r'^admin/', admin.site.urls),
]
