"""Url configuration for Magiokis Verhalen Django version
"""
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^doe/$', views.doe),
    url(r'^(?P<wat_te_doen>nweCat)/$', views.doe),
    url(r'^select/cat/$', views.selcat),
    url(r'^select/cat/sel/$', views.selcat),
    url(r'^select/cat/(?P<zoekdata>\d+)/$', views.selcat),
    url(r'^select/zoek/$', views.selzoek),
    url(r'^select/zoek/(?P<zoekdata>(\b|\w)+)/$', views.selzoek),
    url(r'^detail/$', views.detail),
    url(r'^detail/(?P<item>(nieuw|add))/$', views.detail),
    url(r'^detail/(?P<item>nieuw)/(?P<rubr>cat)/(?P<data>\d+)/$', views.detail),
    url(r'^detail/(?P<item>nieuw)/(?P<rubr>titel)/(?P<data>(\b|\w)+)/$', views.detail),
    url(r'^detail/(?P<item>\d+)/$', views.detail),
    url(r'^detail/(?P<item>\d+)/(?P<rubr>cat)/(?P<data>\d+)/$', views.detail),
    url(r'^detail/(?P<item>\d+)/(?P<rubr>cat)/(?P<data>\d+)/(?P<readonly>lees)/$',
        views.detail),
    url(r'^detail/(?P<item>\d+)/(?P<rubr>titel)/(?P<data>(\b|\w)+)/$', views.detail),
    url(r'^detail/(?P<item>\d+)/(?P<rubr>titel)/(?P<data>(\b|\w)+)/(?P<readonly>lees)/$',
        views.detail),
    url(r'^detail/(?P<item>\d+)/(?P<actie>(lees|wijzig|kies|nieuw))/$', views.detail),
    url(r'^detail/(?P<item>\d+)/(?P<hstuk>\d+)/(?P<actie>wijzig)/$', views.detail),

    # Uncomment this for admin:
    #     url(r'^admin/', include('django.contrib.admin.urls')),
]
