"""Url configuration for Magiokis Verhalen Django version
"""
from django.conf.urls import *

urlpatterns = patterns(
    'magiokis.vertel.views',
    url(r'^$', 'index'),
    url(r'^doe/$', 'doe'),
    url(r'^(?P<wat_te_doen>nweCat)/$', 'doe'),
    url(r'^select/cat/$', 'selcat'),
    url(r'^select/cat/sel/$', 'selcat'),
    url(r'^select/cat/(?P<zoekdata>\d+)/$', 'selcat'),
    url(r'^select/zoek/$', 'selzoek'),
    url(r'^select/zoek/(?P<zoekdata>(\b|\w)+)/$', 'selzoek'),
    url(r'^detail/$', 'detail'),
    url(r'^detail/(?P<item>(nieuw|add))/$', 'detail'),
    url(r'^detail/(?P<item>nieuw)/(?P<rubr>cat)/(?P<data>\d+)/$', 'detail'),
    url(r'^detail/(?P<item>nieuw)/(?P<rubr>titel)/(?P<data>(\b|\w)+)/$', 'detail'),
    url(r'^detail/(?P<item>\d+)/$', 'detail'),
    url(r'^detail/(?P<item>\d+)/(?P<rubr>cat)/(?P<data>\d+)/$', 'detail'),
    url(r'^detail/(?P<item>\d+)/(?P<rubr>cat)/(?P<data>\d+)/(?P<readonly>lees)/$',
     'detail'),
    url(r'^detail/(?P<item>\d+)/(?P<rubr>titel)/(?P<data>(\b|\w)+)/$', 'detail'),
    url(r'^detail/(?P<item>\d+)/(?P<rubr>titel)/(?P<data>(\b|\w)+)/(?P<readonly>lees)/$',
     'detail'),
    url(r'^detail/(?P<item>\d+)/(?P<actie>(lees|wijzig|kies|nieuw))/$', 'detail'),
    url(r'^detail/(?P<item>\d+)/(?P<hstuk>\d+)/(?P<actie>wijzig)/$', 'detail'),

    # Uncomment this for admin:
    #     url(r'^admin/', include('django.contrib.admin.urls')),
)
