from django.conf.urls.defaults import *

urlpatterns = patterns('magiokis.denk.views',
    (r'^$',                                                         'index'),
    (r'^trefw/ok/(?P<trefw>(\w|\b)+)/$',                            'index'),
    (r'^select/(?P<option>(all|trefw|zoek1|zoek2))/$',              'select'),
    (r'^select/(?P<option>trefw)/(?P<trefw>\d+)/$',                 'select'),
    (r'^select/(?P<option>(zoek1|zoek2))/(?P<data>(\w|\b)+)/$',     'select'),
    (r'^enter/(?P<option>(trefw|zoek1|zoek2))/$',                   'enter'),
    (r'^trefw/(?P<option>(nieuw|add))/$',                           'enter'),
    (r'^trefw/(?P<option>(nieuw|add))/(?P<tekst>\d+)/$',            'enter'),
    (r'^detail/$',                                                  'detail'),
    (r'^detail/(?P<option>(nieuw|add))/$',                          'detail'),
    (r'^detail/(?P<tekst>\d+)/$',                                   'detail'),
    (r'^detail/(?P<tekst>\d+)/(?P<option>update)/$',                'detail'),
    (r'^detail/(?P<tekst>\d+)/(?P<option>ok)/(?P<trefw>(\w|\b)+)/$','detail'),
    (r'^detail/(?P<tekst>\d+)/(?P<seltype>\w+)/$',                  'detail'),
    (r'^detail/(?P<tekst>\d+)/(?P<seltype>\w+)/(?P<seldata>\w+)/$', 'detail'),

    # Uncomment this for admin:
#     (r'^admin/', include('django.contrib.admin.urls')),
)