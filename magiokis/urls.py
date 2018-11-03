"""Url configuration for Magiokis Webapps Django version
"""
from django.conf.urls import url, include
from . import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Example:
    # url(r'^magiokis/', include('magiokis.foo.urls')),
    url(r'^$', views.index),
    url(r'^denk/', include('magiokis.denk.urls')),
    url(r'^vertel/', include('magiokis.vertel.urls')),
    url(r'^songs/', include('magiokis.songs.urls')),
    # Uncomment this for admin:
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # media - static files to be served from development server
    # url(r'^xspf_player/(?P<path>.*)$', 'django.views.static.serve',
    #    {'document_root': '/home/albert/xspf_player'}),
    # url(r'^files/(?P<path>.*)$', 'django.views.static.serve',
    #    {'document_root': '/home/albert/django/pythoneer/files'}),
    # url( r'^mp3/(?P<path>.*)$', 'django.views.static.serve',
    #    {'document_root': '/home/albert/music/mp3'}),
    # url(r'^med/(?P<path>.*)$', 'django.views.static.serve',
    #    {'document_root': '/home/albert/music/med'}),
    # url(r'^mid/(?P<path>.*)$', 'django.views.static.serve',
    #    {'document_root': '/home/albert/music/mid'}),
    # url(r'^mod/(?P<path>.*)$', 'django.views.static.serve',
    #    {'document_root': '/home/albert/music/mod'}),
    # url(r'^xm/(?P<path>.*)$', 'django.views.static.serve',
    #    {'document_root': '/home/albert/music/xm'}),
    # url(r'^mm/(?P<path>.*)$', 'django.views.static.serve',
    #    {'document_root': '/home/albert/music/mm'}),
]
