"""Url configuration for Magiokis Webapps Django version
"""
from django.conf.urls import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Example:
    # (r'^magiokis/', include('magiokis.foo.urls')),
    (r'^$', 'magiokis.views.index'),
    (r'^denk/', include('magiokis.denk.urls')),
    (r'^vertel/', include('magiokis.vertel.urls')),
    (r'^songs/', include('magiokis.songs.urls')),
    # Uncomment this for admin:
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # media - static files to be served from development server
    # (r'^xspf_player/(?P<path>.*)$', 'django.views.static.serve',
    #    {'document_root': '/home/albert/xspf_player'}),
    # (r'^files/(?P<path>.*)$', 'django.views.static.serve',
    #    {'document_root': '/home/albert/django/pythoneer/files'}),
    # ( r'^mp3/(?P<path>.*)$', 'django.views.static.serve',
    #    {'document_root': '/home/albert/music/mp3'}),
    # (r'^med/(?P<path>.*)$', 'django.views.static.serve',
    #    {'document_root': '/home/albert/music/med'}),
    # (r'^mid/(?P<path>.*)$', 'django.views.static.serve',
    #    {'document_root': '/home/albert/music/mid'}),
    # (r'^mod/(?P<path>.*)$', 'django.views.static.serve',
    #    {'document_root': '/home/albert/music/mod'}),
    # (r'^xm/(?P<path>.*)$', 'django.views.static.serve',
    #    {'document_root': '/home/albert/music/xm'}),
    # (r'^mm/(?P<path>.*)$', 'django.views.static.serve',
    #    {'document_root': '/home/albert/music/mm'}),
)
