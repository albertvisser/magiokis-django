"""Register Denk models to the site admin
"""
from django.contrib import admin
import magiokis.denk.models as my

admin.site.register(my.Trefw)
admin.site.register(my.Denksel)
