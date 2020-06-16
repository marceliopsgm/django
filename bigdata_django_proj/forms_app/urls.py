from django.conf.urls import url
from forms_app import views

app_name = 'forms_app'

urlpatterns = [
    # url(r'^signup/$', views.signup, name='signup'),

    url(r'^1p_list/$', views.Meta1PListView.as_view(), name='1p_list'),
    url(r'^1p_create/$', views.Meta1PCreateView.as_view(), name='1p_create'),
    url(r'^1p_upload/$', views.meta1pUpload, name='1p_upload'),

    url(r'^3p_list/$', views.Meta3PListView.as_view(), name='3p_list'),
    url(r'^3p_create/$', views.Meta3PCreateView.as_view(), name='3p_create'),
    url(r'^3p_upload/$', views.meta3pUpload, name='3p_upload'),
]