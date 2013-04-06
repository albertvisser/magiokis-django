from django.conf.urls.defaults import *

urlpatterns = patterns('magiokis.vertel.views',
    (r'^$',                                                           'index'),
    (r'^doe/$',                                                       'doe'),
    (r'^(?P<wat_te_doen>nweCat)/$',                                   'doe'),
    (r'^select/cat/$',                                                'selcat'),
    (r'^select/cat/sel/$',                                            'selcat'),
    (r'^select/cat/(?P<zoekdata>\d+)/$',                              'selcat'),
    (r'^select/zoek/$',                                               'selzoek'),
    (r'^select/zoek/(?P<zoekdata>(\b|\w)+)/$',                        'selzoek'),
    (r'^detail/$',                                                    'detail'),
    (r'^detail/(?P<item>(nieuw|add))/$',                              'detail'),
    (r'^detail/(?P<item>nieuw)/(?P<rubr>cat)/(?P<data>\d+)/$',        'detail'),
    (r'^detail/(?P<item>nieuw)/(?P<rubr>titel)/(?P<data>(\b|\w)+)/$', 'detail'),
    (r'^detail/(?P<item>\d+)/$',                                      'detail'),
    (r'^detail/(?P<item>\d+)/(?P<rubr>cat)/(?P<data>\d+)/$',          'detail'),
    (r'^detail/(?P<item>\d+)/(?P<rubr>cat)/(?P<data>\d+)/(?P<readonly>lees)/$',          'detail'),
    (r'^detail/(?P<item>\d+)/(?P<rubr>titel)/(?P<data>(\b|\w)+)/$',   'detail'),
    (r'^detail/(?P<item>\d+)/(?P<rubr>titel)/(?P<data>(\b|\w)+)/(?P<readonly>lees)/$',   'detail'),
    (r'^detail/(?P<item>\d+)/(?P<actie>(lees|wijzig|kies|nieuw))/$',  'detail'),
    (r'^detail/(?P<item>\d+)/(?P<hstuk>\d+)/(?P<actie>wijzig)/$',     'detail'),

    # Uncomment this for admin:
#     (r'^admin/', include('django.contrib.admin.urls')),
)
