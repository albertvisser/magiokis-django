"""Url configuration for Magiokis Songs Django version
"""
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^select/$', views.songlist),
    url(r'^select/(?P<soort>(letter|jaar|search))/$', views.songlist),
    url(r'^select/(?P<soort>(letter|jaar|search))/(?P<data>(\w|\s)+)/$', views.songlist),
    url(r'^select/opnames/$', views.opnlist),
    url(r'^select/opnames/(?P<item>\d+)/$', views.opnlist),
    url(r'^select/regs/$', views.reglist),
    url(r'^select/regs/(?P<item>\d+)/$', views.reglist),
    url(r'^select/series/$', views.series),
    url(r'^detail/(?P<action>add)/$', views.detail),
    url(r'^detail/(?P<item>\d+)/$', views.detail),
    url(r'^detail/(?P<item>\d+)/(?P<soort>(jaar|letter|search))/(?P<sel>(\w|\s)+)/$',
        views.detail),
    url(r'^detail/(?P<item>\d+)/(?P<action>edit)/$', views.detail),
    url(r'^detail/(?P<item>\d+)/(?P<action>edit)/(?P<soort>(jaar|letter|search))/'
        '(?P<sel>(\w|\s)+)/$', views.detail),
    url(r'^detail/(?P<item>\d+)/update/$', views.wijzigdetail),
    url(r'^detail/(?P<item>\d+)/update/(?P<soort>(jaar|letter|search))/'
        '(?P<sel>(\w|\s)+)/$', views.wijzigdetail),
    url(r'^tekst/(?P<item>\d+)/(?P<action>(add|edit))/$', views.wijzigtekst),
    url(r'^tekst/(?P<item>\d+)/(?P<action>(add|edit))/(?P<soort>(jaar|letter|search))/'
        '(?P<sel>(\w|\s)+)/$', views.wijzigtekst),
    url(r'^tekst/(?P<item>\d+)/update/$', views.wijzigtekst),
    url(r'^tekst/(?P<item>\d+)/update/(?P<soort>(jaar|letter|search))/'
        '(?P<sel>(\w|\s)+)/$', views.wijzigtekst),
    url(r'^(?P<item>\d+)/opname/(?P<action>add)/$', views.opname),
    url(r'^(?P<item>\d+)/opname/(?P<action>add)/(?P<soort>(jaar|letter|search))/'
        '(?P<sel>(\w|\s)+)/$', views.opname),
    url(r'^(?P<item>\d+)/opname/(?P<action>add)/(?P<melding>(\w|\s)+)$', views.opname),
    # url(r'^(?P<song>\d+)/opname/(?P<item>\d+)/$',   views.opname),
    # url(r'^(?P<song>\d+)/opname/(?P<item>\d+)/update/$', views.wijzigopname),
    # url(r'^(?P<song>\d+)/opname/play/(?P<item>\w+)/$', 'playopname'),
    url(r'^opname/(?P<item>\d+)/$', views.opname),
    url(r'^opname/(?P<item>\d+)/(?P<soort>(jaar|letter|search))/(?P<sel>(\w|\s)+)/$',
        views.opname),
    url(r'^opname/(?P<item>\d+)/update/$', views.wijzigopname),
    url(r'^opname/(?P<item>\d+)/update/(?P<soort>(jaar|letter|search))/'
        '(?P<sel>(\w|\s)+)/$', views.wijzigopname),
    # url(r'^opname/play/(?P<item>\w+)/$', 'playopname'), -- vervangen door xspf player
    url(r'^(?P<item>\d+)/reg/(?P<action>add)/$', views.reg),
    url(r'^(?P<item>\d+)/reg/(?P<action>add)/(?P<soort>(jaar|letter|search))/'
        '(?P<sel>(\w|\s)+)/$', views.reg),
    # (r'^(?P<song>\d+)/reg/(?P<item>\d+)/$',   views.reg),
    # (r'^(?P<song>\d+)/reg/(?P<item>\d+)/update/$', views.wijzigreg),
    # (r'^(?P<song>\d+)/reg/play/(?P<item>\w+)/$', 'playreg'),
    url(r'^reg/(?P<item>\d+)/$', views.reg),
    url(r'^reg/(?P<item>\d+)/(?P<soort>(jaar|letter|search))/(?P<sel>(\w|\s)+)/$',
        views.reg),
    url(r'^reg/(?P<item>\d+)/update/$', views.wijzigreg),
    url(r'^reg/(?P<item>\d+)/update/(?P<soort>(jaar|letter|search))/'
        '(?P<sel>(\w|\s)+)/$', views.wijzigreg),
    url(r'^reg/show/(?P<item>\w+)/$', views.showreg),
    url(r'^reg/show/(?P<item>\w+)/(?P<page>\w+)/$', views.showreg),
    url(r'^tabel/(?P<soort>\w+)/$', views.tabel),
    url(r'^tabel/(?P<soort>\w+)/(?P<item>\d+)/update/$', views.wijzigtabel),
    url(r'^tabel/(?P<soort>\w+)/add/$', views.wijzigtabel),
    # url(r'^play/(?P<type>\w+)/(?P<id>\d+)/(?P<titel>\d+)/$',        'playurl'),

    # Uncomment this for admin:
    # url(r'^admin/', include('django.contrib.admin.urls')),
]
