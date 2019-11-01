"""Register Denk models to the site admin
"""
from django.contrib import admin
import magiokis.vertel.models as my

admin.site.register(my.Verteller)
admin.site.register(my.Verhaal)
admin.site.register(my.Hoofdstuk)
admin.site.register(my.Bundel)
