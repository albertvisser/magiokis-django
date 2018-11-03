"""Url configuration for Magiokis Denk Django version
"""
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^trefw/ok/(?P<trefw>(\w|\b)+)/$', views.index),
    url(r'^select/(?P<option>(all|trefw|titel|tekst))/$', views.select),
    url(r'^select/(?P<option>trefw)/(?P<trefw>\d+)/$', views.select),
    url(r'^select/(?P<option>(titel|tekst))/(?P<data>(\w|\b)+)/$', views.select),
    url(r'^enter/(?P<option>(trefw|titel|tekst))/$', views.enter),
    url(r'^trefw/(?P<option>(nieuw|add))/$', views.enter),
    url(r'^trefw/(?P<option>(nieuw|add))/(?P<tekst>\d+)/$', views.enter),
    url(r'^detail/$', views.detail),
    url(r'^detail/(?P<option>(nieuw|add))/$', views.detail),
    url(r'^detail/(?P<tekst>\d+)/$', views.detail),
    url(r'^detail/(?P<tekst>\d+)/(?P<option>update)/$', views.detail),
    url(r'^detail/(?P<tekst>\d+)/(?P<option>ok)/(?P<trefw>(\w|\b)+)/$', views.detail),
    url(r'^detail/(?P<tekst>\d+)/(?P<seltype>\w+)/$', views.detail),
    url(r'^detail/(?P<tekst>\d+)/(?P<seltype>\w+)/(?P<seldata>\w+)/$', views.detail),

    # Uncomment this for admin:
    #     url(r'^admin/', include('django.contrib.admin.urls')),
]
