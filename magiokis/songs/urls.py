from django.conf.urls import *

urlpatterns = patterns('magiokis.songs.views',
    (r'^$', 'index'),
    (r'^select/$',                                               'songlist'),
    (r'^select/(?P<soort>(letter|jaar|search))/$',               'songlist'),
    (r'^select/(?P<soort>(letter|jaar|search))/(?P<data>(\w|\s)+)/$', 'songlist'),
    (r'^select/opnames/$',               'opnlist'),
    (r'^select/opnames/(?P<item>\d+)/$', 'opnlist'),
    (r'^select/regs/$',               'reglist'),
    (r'^select/regs/(?P<item>\d+)/$', 'reglist'),
    (r'^select/series/$', 'series'),
    (r'^detail/(?P<action>add)/$',                'detail'),
    (r'^detail/(?P<item>\d+)/$',                  'detail'),
    (r'^detail/(?P<item>\d+)/(?P<action>edit)/$', 'detail'),
    (r'^detail/(?P<item>\d+)/(?P<soort>(jaar|letter|search))/(?P<sel>(\w|\s)+)/$',
        'detail'),
    (r'^detail/(?P<item>\d+)/update/$', 'wijzigdetail'),
    (r'^tekst/(?P<item>\d+)/(?P<action>(add|edit))/$', 'wijzigtekst'),
    (r'^tekst/(?P<item>\d+)/update/$',  'wijzigtekst'),
    (r'^(?P<item>\d+)/opname/(?P<action>add)/$', 'opname'),
    ## (r'^(?P<song>\d+)/opname/(?P<item>\d+)/$',   'opname'),
    ## (r'^(?P<song>\d+)/opname/(?P<item>\d+)/update/$', 'wijzigopname'),
    ## # (r'^(?P<song>\d+)/opname/play/(?P<item>\w+)/$', 'playopname'),
    (r'^opname/(?P<item>\d+)/$',                 'opname'),
    (r'^opname/(?P<item>\d+)/update/$', 'wijzigopname'),
    # (r'^opname/play/(?P<item>\w+)/$', 'playopname'), -- vervangen door xspf player
    (r'^(?P<item>\d+)/reg/(?P<action>add)/$', 'reg'),
    ## (r'^(?P<song>\d+)/reg/(?P<item>\d+)/$',   'reg'),
    ## (r'^(?P<song>\d+)/reg/(?P<item>\d+)/update/$', 'wijzigreg'),
    ## (r'^(?P<song>\d+)/reg/play/(?P<item>\w+)/$', 'playreg'),
    (r'^reg/(?P<item>\d+)/$',                 'reg'),
    (r'^reg/(?P<item>\d+)/update/$', 'wijzigreg'),
    # (r'^reg/play/(?P<item>\w+)/$', 'playreg'),  # dit is meer een "open/download" link
    # maar die zijn vervangen naar een directe link op data.magiokis.nl
    (r'^tabel/(?P<soort>\w+)/$', 'tabel'),
    (r'^tabel/(?P<soort>\w+)/(?P<item>\d+)/update/$', 'wijzigtabel'),
    (r'^tabel/(?P<soort>\w+)/add/$',                  'wijzigtabel'),
    #~ (r'^play/(?P<type>\w+)/(?P<id>\d+)/(?P<titel>\d+)/$',        'playurl'),

    # Uncomment this for admin:
#     (r'^admin/', include('django.contrib.admin.urls')),
)
