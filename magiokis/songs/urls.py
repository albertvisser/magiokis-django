"""Url configuration for Magiokis Songs Django version
"""
from django.conf.urls import *

urlpatterns = patterns(
    'magiokis.songs.views',
    url(r'^$', 'index'),
    url(r'^select/$', 'songlist'),
    url(r'^select/(?P<soort>(letter|jaar|search))/$', 'songlist'),
    url(r'^select/(?P<soort>(letter|jaar|search))/(?P<data>(\w|\s)+)/$', 'songlist'),
    url(r'^select/opnames/$', 'opnlist'),
    url(r'^select/opnames/(?P<item>\d+)/$', 'opnlist'),
    url(r'^select/regs/$', 'reglist'),
    url(r'^select/regs/(?P<item>\d+)/$', 'reglist'),
    url(r'^select/series/$', 'series'),
    url(r'^detail/(?P<action>add)/$', 'detail'),
    url(r'^detail/(?P<item>\d+)/$', 'detail'),
    url(r'^detail/(?P<item>\d+)/(?P<soort>(jaar|letter|search))/(?P<sel>(\w|\s)+)/$',
     'detail'),
    url(r'^detail/(?P<item>\d+)/(?P<action>edit)/$', 'detail'),
    url(r'^detail/(?P<item>\d+)/(?P<action>edit)/(?P<soort>(jaar|letter|search))/'
     '(?P<sel>(\w|\s)+)/$', 'detail'),
    url(r'^detail/(?P<item>\d+)/update/$', 'wijzigdetail'),
    url(r'^detail/(?P<item>\d+)/update/(?P<soort>(jaar|letter|search))/'
     '(?P<sel>(\w|\s)+)/$', 'wijzigdetail'),
    url(r'^tekst/(?P<item>\d+)/(?P<action>(add|edit))/$', 'wijzigtekst'),
    url(r'^tekst/(?P<item>\d+)/(?P<action>(add|edit))/(?P<soort>(jaar|letter|search))/'
     '(?P<sel>(\w|\s)+)/$', 'wijzigtekst'),
    url(r'^tekst/(?P<item>\d+)/update/$', 'wijzigtekst'),
    url(r'^tekst/(?P<item>\d+)/update/(?P<soort>(jaar|letter|search))/'
     '(?P<sel>(\w|\s)+)/$', 'wijzigtekst'),
    url(r'^(?P<item>\d+)/opname/(?P<action>add)/$', 'opname'),
    url(r'^(?P<item>\d+)/opname/(?P<action>add)/(?P<soort>(jaar|letter|search))/'
     '(?P<sel>(\w|\s)+)/$', 'opname'),
    url(r'^(?P<item>\d+)/opname/(?P<action>add)/(?P<melding>(\w|\s)+)$', 'opname'),
    # url(r'^(?P<song>\d+)/opname/(?P<item>\d+)/$',   'opname'),
    # url(r'^(?P<song>\d+)/opname/(?P<item>\d+)/update/$', 'wijzigopname'),
    # url(r'^(?P<song>\d+)/opname/play/(?P<item>\w+)/$', 'playopname'),
    url(r'^opname/(?P<item>\d+)/$', 'opname'),
    url(r'^opname/(?P<item>\d+)/(?P<soort>(jaar|letter|search))/(?P<sel>(\w|\s)+)/$',
     'opname'),
    url(r'^opname/(?P<item>\d+)/update/$', 'wijzigopname'),
    url(r'^opname/(?P<item>\d+)/update/(?P<soort>(jaar|letter|search))/'
     '(?P<sel>(\w|\s)+)/$', 'wijzigopname'),
    # url(r'^opname/play/(?P<item>\w+)/$', 'playopname'), -- vervangen door xspf player
    url(r'^(?P<item>\d+)/reg/(?P<action>add)/$', 'reg'),
    url(r'^(?P<item>\d+)/reg/(?P<action>add)/(?P<soort>(jaar|letter|search))/'
     '(?P<sel>(\w|\s)+)/$', 'reg'),
    # (r'^(?P<song>\d+)/reg/(?P<item>\d+)/$',   'reg'),
    # (r'^(?P<song>\d+)/reg/(?P<item>\d+)/update/$', 'wijzigreg'),
    # (r'^(?P<song>\d+)/reg/play/(?P<item>\w+)/$', 'playreg'),
    url(r'^reg/(?P<item>\d+)/$', 'reg'),
    url(r'^reg/(?P<item>\d+)/(?P<soort>(jaar|letter|search))/(?P<sel>(\w|\s)+)/$',
     'reg'),
    url(r'^reg/(?P<item>\d+)/update/$', 'wijzigreg'),
    url(r'^reg/(?P<item>\d+)/update/(?P<soort>(jaar|letter|search))/'
     '(?P<sel>(\w|\s)+)/$', 'wijzigreg'),
    url(r'^reg/show/(?P<item>\w+)/$', 'showreg'),
    url(r'^reg/show/(?P<item>\w+)/(?P<page>\w+)/$', 'showreg'),
    url(r'^tabel/(?P<soort>\w+)/$', 'tabel'),
    url(r'^tabel/(?P<soort>\w+)/(?P<item>\d+)/update/$', 'wijzigtabel'),
    url(r'^tabel/(?P<soort>\w+)/add/$', 'wijzigtabel'),
    # url(r'^play/(?P<type>\w+)/(?P<id>\d+)/(?P<titel>\d+)/$',        'playurl'),

    # Uncomment this for admin:
    # url(r'^admin/', include('django.contrib.admin.urls')),
)
