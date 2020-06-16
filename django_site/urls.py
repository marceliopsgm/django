"""django_site URL Configuration

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
from django.urls import path, include

from django_site.metas_app import views
from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),

    url(r'^1p_list/$', views.Meta1PListView.as_view(), name='1p_list'),
    url(r'^1p_create/$', views.Meta1PCreateView.as_view(), name='1p_create'),
    url(r'^1p_upload/$', views.meta1pUpload, name='1p_upload'),

    url(r'^3p_list/$', views.Meta3PListView.as_view(), name='3p_list'),
    url(r'^3p_create/$', views.Meta3PCreateView.as_view(), name='3p_create'),
    url(r'^3p_upload/$', views.meta3pUpload, name='3p_upload'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
