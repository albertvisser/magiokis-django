﻿"""Web views for Magiokis Denk Django version
"""
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
import magiokis.denk.models as my


def index(request, trefw=None):
    """Landing page of webapp
    """
    page_data = {"message": "",
                 "crumbs": [('/', 'Home', 'Magiokis'),
                            ('/denk/', 'start', "denk: start")]}
    page_data["title"] = "Start"
    if trefw is not None:
        page_data["message"] = 'trefwoord "%s" is opgevoerd' % trefw
    else:
        page_data["message"] = ""
    return render(request, 'denk/start.html', page_data)


def select(request, option='', trefw=None, data=None):
    """Selection page
    """
    page_data = {"message": "",
                 "crumbs": [('/', 'Home', 'Magiokis'),
                            ('/denk/', 'start', "denk: start")]}
    page_data["title"] = "Select by " + option
    input_dict = request.GET if request.method == 'GET' else {}
    selectie = []
    if option == 'all':
        page_data["crumbs"].append((request.path, "alle teksten", "denk: alle teksten"))
        titel = "Overzicht alle bedenksels"
        page_data["hier"] = 'alles'
        selectie = my.Denksel.objects.all()
    elif option == 'trefw':
        if trefw is None:
            trefw = input_dict.get("lbSelItem", '')
            return HttpResponseRedirect('/denk/select/trefw/{}/'.format(trefw))
        page_data["crumbs"].append(('/denk/enter/trefw/', "op trefwoord",
                                    "denk: enter trefwoord"))
        page_data["crumbs"].append((request.path, "selectie",
                                    "denk: teksten bij trefwoord"))
        data = my.Trefw.objects.get(id=trefw)
        titel = 'Overzicht bedenksels bij trefwoord "%s"' % data
        page_data["hier"] = 'trefw/%s/' % trefw
        selectie = my.Denksel.objects.filter(trefwoorden=trefw)
    elif option == 'titel':
        if data is None:
            data = input_dict.get("txtInput", '')
            return HttpResponseRedirect('/denk/select/titel/{}/'.format(data))
        page_data["crumbs"].append(('/denk/enter/titel', "op titel", "denk: zoeken in titel "))
        page_data["crumbs"].append((request.path, "selectie", "denk: teksten op titeldeel "))
        titel = 'Overzicht bedenksels met "%s" in titel' % data
        page_data["hier"] = 'titel/%s/' % data
        selectie = my.Denksel.objects.filter(titel__icontains=data)
    elif option == 'tekst':
        if data is None:
            data = input_dict.get("txtInput", '')
            return HttpResponseRedirect('/denk/select/tekst/{}/'.format(data))
        page_data["crumbs"].append(('/denk/enter/tekst', "op tekst", "denk: zoeken in tekst"))
        page_data["crumbs"].append((request.path, "selectie", "denk: teksten op tekstdeel"))
        titel = 'Overzicht bedenksels met "%s" in tekst' % data
        page_data["hier"] = 'tekst/%s/' % data
        selectie = my.Denksel.objects.filter(tekst__icontains=data)
    else:
        return HttpResponse('"%(option)s" niet gedefinieerd bij "%(where)s"')
    page_data['subtitle'] = titel
    page_data['selection'] = selectie
    if not selectie:
        page_data["message"] = '(Nog) geen bedenksels aanwezig'
    return render(request, 'denk/select_list.html', page_data)


def enter(request, option='', tekst=''):
    """View for pages where something can be entered
    """
    page_data = {"message": "",
                 "crumbs": [('/', 'Home', 'Magiokis'),
                            ('/denk/', 'start', "denk: start")],
                 "rest": ""}
    page_data["title"] = "Enter Search Argument"  # + option
    page_data["reqtype"] = 'get'
    if option == 'trefw':
        page_data["crumbs"].append((request.path, "op trefwoord", "denk: enter trefwoord"))
        titel = "Kies een trefwoord uit de lijst"
        page_data["selection"] = my.Trefw.objects.all().order_by('woord')
    elif option in ('titel', 'tekst'):
        if option == 'titel':
            page_data["crumbs"].append((request.path, "op titel", "denk: zoeken in titel "))
        else:
            page_data["crumbs"].append((request.path, "op tekst", "denk: zoeken in tekst"))
        page_data["next"] = '/denk/select/%s/' % option
        titel = "Geef een zoektekst op"
        zoek_in = 'titel' if option == 'titel' else 'tekst'
        page_data["subtext"] = "Zoek in %s" % zoek_in
    elif option in ('nieuw', 'add'):
        page_data["rest"] = my.Trefw.objects.all().order_by('woord')
        if option == 'add':
            nw_trefw = request.POST.get('txtInput', '') if request.method == 'POST' else ''
            dubbel = True
            try:
                my.Trefw.objects.get(woord=nw_trefw)
            except ObjectDoesNotExist:
                dubbel = False
            if dubbel:
                page_data["crumbs"].append(('/denk/trefw/nieuw/', "nieuw trefwoord",
                                            "denk: nieuw trefwoord"))
                page_data["message"] = 'trefwoord "%s" bestaat al' % nw_trefw
                if tekst:
                    page_data["next"] = '/denk/trefw/add/%s/' % tekst
                else:
                    page_data["next"] = '/denk/trefw/add/'
                page_data["reqtype"] = "post"
            else:
                ## tw = my.Trefw.objects.create(woord=nw_trefw)
                if tekst:
                    return HttpResponseRedirect('/denk/detail/%s/ok/%s/' % (tekst, nw_trefw))
                return HttpResponseRedirect('/denk/trefw/ok/%s/' % nw_trefw)
        else:
            page_data["crumbs"].append((request.path, "nieuw trefwoord", "denk: nieuw trefwoord"))
            page_data["next"] = '/denk/trefw/add/'
            page_data["reqtype"] = "post"
            if tekst:
                page_data["next"] = tekst.join((page_data["next"], '/'))
        titel = "Geef een nieuw trefwoord op"
        page_data["subtext"] = "Opvoeren"
    else:
        return HttpResponse('"%(option)s" niet gedefinieerd bij "%(where)s"')
    page_data['subtitle'] = titel
    page = 'denk/select_args.html' if option == "trefw" else 'denk/input_args.html'
    return render(request, page, page_data)


def detail(request, tekst='', option='', seltype='', seldata='', trefw=''):
    """View for details page (also in edit mode)
    """
    page_data = {"message": "",
                 "crumbs": [('/', 'Home', 'Magiokis'),
                            ('/denk/', 'start', "denk: start")],
                 "knoptekst": "Nieuwe opvoeren"}
    ## data = request.path.split('/')
    denk_id = int(tekst)
    if not seltype and "hselopt" in request.POST:  # moet dit 'selopt' in request.GET worden?
        test = request.POST["hselopt"].split("/")
        seltype = test[0]
        if len(test) > 1:
            seldata = test[1]
    page_data["zoek"] = seltype
    if seldata:
        page_data["zoek"] = "/".join((seltype, seldata))
    if seltype == "alles":
        page_data["crumbs"].append(('/denk/select/all/', 'alle teksten', 'denk: alle teksten'))
    elif seltype == "trefw":
        page_data["crumbs"].append(('/denk/enter/trefw/', "op trefwoord", "denk: enter trefwoord"))
        page_data["crumbs"].append(('/denk/select/trefw/%s' % seldata, "selectie",
                                    "denk: teksten bij trefwoord"))
    elif seltype == "zoek1":
        page_data["crumbs"].append(('/denk/enter/zoek1', "op titel", "denk: zoeken in titel "))
        page_data["crumbs"].append(('/denk/select/zoek1/%s' % seldata, "selectie",
                                    "denk: teksten op titeldeel "))
    elif seltype == "zoek2":
        page_data["crumbs"].append(('/denk/enter/zoek2', "op tekst", "denk: zoeken in tekst"))
        page_data["crumbs"].append(('/denk/select/zoek2/%s' % seldata, "selectie",
                                    "denk: teksten op tekstdeel"))
    if request.method == 'POST':
        argdict = request.POST
    # elif request.method == 'GET':
    #     argdict = request.GET
    # else:
    #     argdict = {}
    # if argdict:
        denk_id = argdict.get("lbSelItem", '')
        if not denk_id:
            denk_id = argdict.get("hselItem", '')
        denk_titel = argdict.get("txtTitel", '')
        denk_tekst = argdict.get("txtTekst", '')
        h = argdict.get("txtTrefw", '')
        denk_trefw = h.split("$#$") if h else []

    page_data["title"] = "Detail " + option
    if option == 'ok':
        page_data["message"] = 'trefwoord "%s" is opgevoerd' % trefw
    if option == 'nieuw' or (option == 'ok' and tekst == '0'):
        page_data["next"] = '/denk/detail/add/'
        page_data["actie"] = "opvoeren"
        page_data["knoptekst"] = "Overnieuw"
        page_data["trefw_ex"] = my.Trefw.objects.all()
        # denk_id = 0
    else:
        if option == 'add' and (denk_titel or denk_tekst):
            d = my.Denksel.objects.create(titel=denk_titel, tekst=denk_tekst)
            d.trefwoorden.clear()
            for x in denk_trefw:
                d.trefwoorden.add(my.Trefw.objects.get(id=x))
            d.save()
            denk_id = d.id
        elif option != 'ok':
            d = my.Denksel.objects.get(id=denk_id)
            if option == "update":
                d.titel = denk_titel
                d.tekst = denk_tekst
                d.trefwoorden.clear()
                for x in denk_trefw:
                    d.trefwoorden.add(my.Trefw.objects.get(id=x))
                d.save()
        page_data["next"] = '/denk/detail/%s/update/' % denk_id
        page_data["actie"] = "wijzigen"
        d = my.Denksel.objects.get(id=denk_id)
        page_data["id"] = d.id
        page_data["titel"] = d.titel
        page_data["tekst"] = d.tekst
        trefw = d.trefwoorden.all().order_by('woord')
        page_data["trefw_in"] = trefw
        page_data["trefw_ex"] = [x for x in my.Trefw.objects.all() if x not in trefw]
    page_data["crumbs"].append(('/denk/detail/%s/' % denk_id, 'tekst', 'deze tekst'))
    return render(request, 'denk/detail.html', page_data)
