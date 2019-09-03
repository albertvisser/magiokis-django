"""Web views for Magiokis Songs Django version
"""
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponseRedirect   # HttpResponse,
from django.shortcuts import render  # , get_object_or_404
import magiokis.vertel.models as my


def index(request, melding=''):
    """Landing page for the webapp
    """
    page_data = {"message": "",
                 "crumbs": [('/', 'Home', 'Magiokis'),
                            ('/vertel/', 'start', "vertel: start")]}
    page_data["title"] = "Start"
    if melding:
        page_data["message"] = melding
    return render(request, 'vertel/start.html', page_data)


def doe(request, melding='', wat_te_doen=''):
    """Dispatcher view
    """
    if request.method == 'POST':
        incoming = request.POST
    else:
        incoming = {}
    ## if 'txtUser' in incoming:
        ## verteller = incoming["txtUser"]
    if wat_te_doen == '':
        wat_te_doen = incoming.get("rbsel", '')
    if wat_te_doen == "selCat":
        return HttpResponseRedirect("/vertel/select/cat/")
    elif wat_te_doen == "selZoek":
        zoekdata = incoming.get("txtZoek", '')
        return HttpResponseRedirect("/vertel/select/zoek/%s/" % zoekdata)
    elif wat_te_doen == "nweTekst":
        return HttpResponseRedirect("/vertel/detail/nieuw/")
    elif wat_te_doen != "nweCat":
        return Http404
    nwe_cat = incoming.get("txtNweCat", '')
    page_data = {"message": "",
                 "crumbs": [('/', 'Home', 'Magiokis'),
                            ('/vertel/', 'start', "vertel: start")]}
    ## page_data["crumbs"].append(('/vertel/nweCat/','nieuwe categorie','vertel: nweCat'))
    ## page_data["title"] = "Nieuw: Cat"
    try:
        my.Bundel.objects.get(titel=nwe_cat)
    except ObjectDoesNotExist:
        my.Bundel.objects.create(titel=nwe_cat)
        page_data["message"] = nwe_cat.join(('nieuwe categorie "', '" opgevoerd'))
    else:
        page_data["message"] = nwe_cat.join(('categorie "', '" bestaat al'))
    return render(request, 'vertel/start.html', page_data)


def selcat(request, zoekdata="", melding=''):
    """Select stories in a category
    """
    if request.method == 'GET':
        incoming = request.GET
    elif request.method == 'POST':
        incoming = request.POST
    # else:
    #     incoming = {}
    if incoming:
        zoekdata = incoming.get("lbSelCat", '')
        return HttpResponseRedirect("/vertel/select/cat/{}/".format(zoekdata))
    page_data = {"message": "",
                 "crumbs": [('/', 'Home', 'Magiokis'),
                            ('/vertel/', 'start', "vertel: start")]}
    page_data["crumbs"].append(('/vertel/select/cat/', 'kies categorie', 'vertel: selCat'))
    page_data["title"] = "Select: Cat"
    page_data["cats"] = my.Bundel.objects.all()
    if melding:
        page_data["message"] = melding
    gevonden = ''
    if zoekdata:
        page_data["crumbs"].append(('/vertel/select/cat/%s/' % zoekdata,
                                    'kies tekst', 'vertel: selCat'))
        cat = my.Bundel.objects.get(id=zoekdata)
        page_data["items"] = my.Verhaal.objects.filter(bundel=zoekdata)
        h = str(len(page_data["items"])) if page_data["items"] else 'Geen'
        gevonden = ' '.join((h, 'verhalen gevonden bij categorie', cat.titel.join(('"', '"'))))
        page_data["nieuw"] = '/vertel/detail/nieuw/cat/%s/' % cat.id
        page_data["rubr"] = "cat"
        page_data["data"] = zoekdata
    page_data['aantal'] = gevonden
    page_data['bij'] = 'bij deze categorie'
    return render(request, 'vertel/select.html', page_data)


def selzoek(request, zoekdata='', melding=''):
    """Select stories containing text
    """
    if request.method == 'GET':
        incoming = request.GET
    elif request.method == 'POST':
        incoming = request.POST
    # else:
    #     incoming = {}
    if incoming:
        zoekdata = incoming.get("txtZoek")
    page_data = {"message": "",
                 "crumbs": [('/', 'Home', 'Magiokis'),
                            ('/vertel/', 'start', "vertel: start")]}
    page_data["crumbs"].append(('/vertel/select/zoek/%s/' % zoekdata,
                                'lijst teksten', 'vertel: selZoek'))
    page_data["title"] = "Select: Zoek"
    if melding:
        page_data["message"] = melding
    gevonden = ''
    if zoekdata:
        page_data["zoek"] = zoekdata
        page_data["items"] = my.Verhaal.objects.filter(titel__icontains=zoekdata)
        h = str(len(page_data["items"])) if page_data["items"] else 'Geen'
        gevonden = ' '.join((h, 'verhalen gevonden met', zoekdata.join(('"', '"')),
                             'in de titel'))
        page_data["nieuw"] = '/vertel/detail/nieuw/titel/%s/' % zoekdata
        page_data["rubr"] = "titel"
        page_data["data"] = zoekdata
    page_data['aantal'] = gevonden
    page_data['bij'] = ''
    return render(request, 'vertel/select.html', page_data)


def detail(request, item=None, melding='', actie='', hstuk=None, rubr='', data='',
           readonly=''):
    """Story contents
    """
    if request.method == 'GET':
        incoming = request.GET
    elif request.method == 'POST':
        incoming = request.POST
    else:
        incoming = {}
    ## r_o = incoming.get("readonly","")
    r_o = True if readonly or actie == 'lees' else False
    page_data = {"message": "",
                 "crumbs": [('/', 'Home', 'Magiokis'),
                            ('/vertel/', 'start', "vertel: start")]}
    extra = data + '/' if data else ''
    if rubr == "cat":
        page_data["crumbs"].append(('/vertel/select/cat/', 'kies categorie',
                                    'vertel: selCat'))
        page_data["crumbs"].append(('/vertel/select/cat/%s' % extra, 'kies tekst',
                                    'vertel: selText'))
        page_data["cat"] = int(data)
        extra = "/cat/{0}".format(data)
    elif rubr == 'titel':
        page_data["crumbs"].append(('/vertel/select/zoek/%s' % extra, 'lijst teksten',
                                    'vertel: selZoek'))
        page_data["nwe_titel"] = data
        extra = "/titel/{0}".format(data)
    else:
        extra = ""
    if item == "nieuw":
        page_data["crumbs"].append(('/vertel/detail{}/nieuw/'.format(extra),
                                    'nieuwe tekst', 'vertel: nieuw'))
        # toon leeg scherm
    ## elif item == "add":
        ## # voer een nieuw verhaal op en onthou de sleutel
        ## titel = incoming["txtTitel"]
        ## cat = incoming["lbSelCat"]
        ## nv = my.Verhaal.objects.create(titel=titel)
        ## nv.bundel = cat
        ## nv.save()
        ## page_data["crumbs"].append(('/vertel/detail/%s/' % item,'tekst','vertel: tekst'))
    else:
        # moet iets verder uitgesplitst worden i.v.m. de verschillende hoofdstukken
        r_o_opt = "" if r_o else "lees/"
        text = "wijzig" if r_o else "bekijk"
        text = "naar `{} tekst`".format(text)
        page_data["crumbs"].append(('/vertel/detail/{}{}/{}'.format(item, extra, r_o_opt),
                                    text, 'vertel: tekst'))
        if r_o:
            h = my.Verhaal.objects.get(id=item)
            page_data["verhaal"] = h
            page_data["hslijst"] = h.hoofdstukken.all()
            page_data["auteur"] = str(h.schrijver)
            return render(request, 'vertel/detail_ro.html', page_data)
        hstuk = incoming.get("selHoofdstuk", '')
        if actie == "wijzig":
            if hstuk:  # hoofdstuk opvoeren/wijzigen
                titel = incoming.get("txtTitel2", '')
                inhoud = incoming.get("txtHoofdstuk", '')
                verhaal = my.Verhaal.objects.get(id=item)
                if hstuk == '0':
                    h = my.Hoofdstuk.objects.create(titel=titel,
                                                    inhoud=inhoud, verhaal=verhaal)
                    hstuk = h.id
                else:
                    h = my.Hoofdstuk.objects.get(id=hstuk)
                    h.titel = titel
                    h.inhoud = inhoud
                    h.save()
            else:  # verhaal opvoeren/wijzigen
                titel = incoming.get("txtTitel", '')
                cat = incoming.get("lbSelCat", '')
                aut = my.Verteller.objects.all()[0]
                if item == '0':
                    h = my.Verhaal(titel=titel, schrijver=aut)
                    h.save()
                    item = h.id
                    hstuk = '0'
                else:
                    h = my.Verhaal.objects.get(id=item)
                    h.titel = incoming["txtTitel"]
                h.bundel = cat
                h.save()
        # verhaal (opnieuw) ophalen
        h = my.Verhaal.objects.get(id=item)
        page_data["cat"] = h.bundel.all()[0].id
        page_data["verhaal"] = h
        ## page_data["cat"] = h.bundel
        hslijst = h.hoofdstukken.all()
        page_data["hslijst"] = hslijst
        if item != "0":
            if not hslijst:
                hstuk = '0'
            elif not hstuk:
                hstuk = hslijst[0].id
            if hstuk != "0":
                page_data["hst"] = my.Hoofdstuk.objects.get(id=hstuk)

    page_data["title"] = "Detail"
    if melding:
        page_data["message"] = melding
    page_data["cats"] = my.Bundel.objects.all()
    return render(request, 'vertel/detail.html', page_data)
