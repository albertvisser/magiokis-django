"""Url configuration for Magiokis Denk Django version
"""
from django.conf.urls import *

urlpatterns = patterns(
    'magiokis.denk.views',
    url(r'^$', 'index'),
    url(r'^trefw/ok/(?P<trefw>(\w|\b)+)/$', 'index'),
    url(r'^select/(?P<option>(all|trefw|titel|tekst))/$', 'select'),
    url(r'^select/(?P<option>trefw)/(?P<trefw>\d+)/$', 'select'),
    url(r'^select/(?P<option>(titel|tekst))/(?P<data>(\w|\b)+)/$', 'select'),
    url(r'^enter/(?P<option>(trefw|titel|tekst))/$', 'enter'),
    url(r'^trefw/(?P<option>(nieuw|add))/$', 'enter'),
    url(r'^trefw/(?P<option>(nieuw|add))/(?P<tekst>\d+)/$', 'enter'),
    url(r'^detail/$', 'detail'),
    url(r'^detail/(?P<option>(nieuw|add))/$', 'detail'),
    url(r'^detail/(?P<tekst>\d+)/$', 'detail'),
    url(r'^detail/(?P<tekst>\d+)/(?P<option>update)/$', 'detail'),
    url(r'^detail/(?P<tekst>\d+)/(?P<option>ok)/(?P<trefw>(\w|\b)+)/$', 'detail'),
    url(r'^detail/(?P<tekst>\d+)/(?P<seltype>\w+)/$', 'detail'),
    url(r'^detail/(?P<tekst>\d+)/(?P<seltype>\w+)/(?P<seldata>\w+)/$', 'detail'),

    # Uncomment this for admin:
    #     url(r'^admin/', include('django.contrib.admin.urls')),
)
