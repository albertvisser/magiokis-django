"""Page views for Magiokis Webapps Django version
"""
## from django.template import Context, loader
## from django.http import HttpResponse
## from django.http import Http404
## from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response  # , get_object_or_404
from magiokis.settings import MEDIA_ROOT


def index(request):
    """Landing page for "root level" above webapp level
    """
    return render_to_response('index.html', {})


def viewdoc(request):
    """view an uploaded file (?)
    """
    parts = request.path.split('files/')
    return render_to_response(MEDIA_ROOT + parts[1], {})
