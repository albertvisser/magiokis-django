## from django.template import Context, loader
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponse, HttpResponseRedirect
import magiokis.vertel.models as my
from django.shortcuts import render_to_response, get_object_or_404

def index(request, melding=''):
    page_data = {"message": "",
                "crumbs": [('/', 'Home', 'Magiokis'),
                            ('/vertel/','start',"vertel: start")]}
    page_data["title"] = "Start"
    if melding:
        page_data["message"] = melding
    return render_to_response('vertel/start.html',page_data)

def doe(request, melding='', wat_te_doen=''):
    try:
        incoming = request.POST
    except:
        incoming = {}
    if 'txtUser' in incoming:
        verteller = incoming["txtUser"]
    if wat_te_doen == '':
        wat_te_doen = incoming["rbsel"]
    if wat_te_doen == "selCat":
        return HttpResponseRedirect("/vertel/select/cat/")
    elif wat_te_doen == "selZoek":
        zoekdata = incoming["txtZoek"]
        return HttpResponseRedirect("/vertel/select/zoek/%s/" % zoekdata)
    elif wat_te_doen == "nweTekst":
        return HttpResponseRedirect("/vertel/detail/nieuw/")
    elif wat_te_doen != "nweCat":
        return Http404
    nwe_cat = incoming["txtNweCat"]
    page_data = {"message": "",
                "crumbs": [('/', 'Home', 'Magiokis'),
                            ('/vertel/','start',"vertel: start")]}
    ## page_data["crumbs"].append(('/vertel/nweCat/','nieuwe categorie','vertel: nweCat'))
    ## page_data["title"] = "Nieuw: Cat"
    try:
        my.Bundel.objects.get(titel=nwe_cat)
    except ObjectDoesNotExist:
        my.Bundel.objects.create(titel=nwe_cat)
        page_data["message"] = nwe_cat.join(('nieuwe categorie "','" opgevoerd'))
    else:
        page_data["message"] = nwe_cat.join(('categorie "','" bestaat al'))
    return render_to_response('vertel/start.html',page_data)

def selcat(request, zoekdata="", melding=''):
    try:
        incoming = request.POST
    except:
        incoming = {}
    page_data = {"message": "",
                "crumbs": [('/', 'Home', 'Magiokis'),
                            ('/vertel/','start',"vertel: start")]}
    page_data["crumbs"].append(('/vertel/select/cat/','kies categorie','vertel: selCat'))
    page_data["title"] = "Select: Cat"
    page_data["cats"] = my.Bundel.objects.all()
    if melding:
        page_data["message"] = melding
    gevonden = ''
    if "lbSelCat" in incoming:
        zoekdata = incoming["lbSelCat"]
    if zoekdata:
        page_data["crumbs"].append(('/vertel/select/cat/%s' % zoekdata,
            'kies tekst','vertel: selCat'))
        cat = my.Bundel.objects.get(id=zoekdata)
        page_data["items"] = my.Verhaal.objects.filter(bundel=zoekdata)
        h = 'Geen' if len(page_data["items"]) == 0 else str(len(page_data["items"]))
        gevonden = ' '.join((h,'verhalen gevonden bij categorie',cat.titel.join(('"','"'))))
        page_data["nieuw"] = '/vertel/detail/nieuw/cat/%s/' % cat.id
        page_data["rubr"] = "cat"
        page_data["data"] = zoekdata
    page_data['aantal'] = gevonden
    page_data['bij'] = 'bij deze categorie'
    return render_to_response('vertel/select.html',page_data)

def selzoek(request, zoekdata='', melding=''):
    try:
        incoming = request.POST
    except:
        incoming = {}
    page_data = {"message": "",
                "crumbs": [('/', 'Home', 'Magiokis'),
                            ('/vertel/','start',"vertel: start")]}
    page_data["crumbs"].append(('/vertel/select/zoek/%s/' % zoekdata,
                            'lijst teksten','vertel: selZoek'))
    page_data["title"] = "Select: Zoek"
    if melding:
        page_data["message"] = melding
    gevonden = ''
    if "txtZoek" in incoming:
        zoekdata = incoming["txtZoek"]
    if zoekdata:
        page_data["zoek"] = zoekdata
        page_data["items"] = my.Verhaal.objects.filter(titel__icontains=zoekdata)
        h = 'Geen' if len(page_data["items"]) == 0 else str(len(page_data["items"]))
        gevonden = ' '.join((h,'verhalen gevonden met',zoekdata.join(('"','"')),'in de titel'))
        page_data["nieuw"] = '/vertel/detail/nieuw/titel/%s/' % zoekdata
        page_data["rubr"] = "titel"
        page_data["data"] = zoekdata
    page_data['aantal'] = gevonden
    page_data['bij'] = ''
    return render_to_response('vertel/select.html',page_data)

def detail(request, item=None, melding='', actie='', hstuk=None, rubr='', data='',
        readonly=''):
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
                            ('/vertel/','start',"vertel: start")]}
    if rubr == "cat":
        page_data["crumbs"].append(('/vertel/select/cat/','kies categorie','vertel: selCat'))
        page_data["crumbs"].append(('/vertel/select/cat/%s' % data,
            'kies tekst','vertel: selCat'))
        page_data["cat"] = int(data)
        extra = "/cat/{0}".format(data)
    elif rubr == 'titel':
        page_data["crumbs"].append(('/vertel/select/zoek/%s/' % data,
                                'lijst teksten','vertel: selZoek'))
        page_data["nwe_titel"] = data
        extra = "/titel/{0}".format(data)
    else:
        extra = ""
    if item == "nieuw":
        page_data["crumbs"].append(('/vertel/detail{0}/nieuw'.format(extra),
            'nieuwe tekst','vertel: nieuw'))
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
        r_o_opt = "" if r_o else "lees"
        text = "wijzig tekst" if r_o else "bekijk tekst"
        page_data["crumbs"].append(('/vertel/detail/{0}{1}/{2}'.format(item,
            extra,r_o_opt),text,'vertel: tekst'))
        if r_o:
            h = my.Verhaal.objects.get(id=item)
            page_data["verhaal"] = h
            page_data["hslijst"] = h.hoofdstukken.all()
            page_data["auteur"] = str(h.schrijver)
            return render_to_response('vertel/detail_ro.html',page_data)
        if "selHoofdstuk" in incoming:
            hstuk =  incoming["selHoofdstuk"]
        if actie == "wijzig":
            if hstuk: # hoofdstuk opvoeren/wijzigen
                titel = incoming["txtTitel2"]
                inhoud = incoming["txtHoofdstuk"]
                verhaal = my.Verhaal.objects.get(id=item)
                if hstuk == '0':
                    h = my.Hoofdstuk.objects.create(titel=titel,
                        inhoud=inhoud,verhaal=verhaal)
                    hstuk = h.id
                else:
                    h = my.Hoofdstuk.objects.get(id=hstuk)
                    h.titel = titel
                    h.inhoud = inhoud
                    h.save()
            else: # verhaal opvoeren/wijzigen
                titel = incoming["txtTitel"]
                cat = incoming["lbSelCat"]
                aut = my.Verteller.objects.all()[0]
                if item == '0':
                    h = my.Verhaal(titel=titel,schrijver=aut)
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
            if len(hslijst) == 0:
                hstuk = '0'
            elif not hstuk:
                hstuk = hslijst[0].id
            if hstuk != "0":
                page_data["hst"] = my.Hoofdstuk.objects.get(id=hstuk)

    page_data["title"] = "Detail"
    if melding:
        page_data["message"] = melding
    page_data["cats"] = my.Bundel.objects.all()
    return render_to_response('vertel/detail.html',page_data)