"""Page views for Magiokis Webapps Django version
"""
## from django.template import Context, loader
## from django.http import HttpResponse
## from django.http import Http404
## from django.http import HttpResponseRedirect
from django.shortcuts import render
from magiokis.settings import MEDIA_ROOT


def index(request):
    """Landing page for "root level" above webapp level
    """
    return render(request, 'index.html', {})


def viewdoc(request):
    """view an uploaded file (?)
    """
    parts = request.path.split('files/')
    return render(request, MEDIA_ROOT + parts[1], {})
