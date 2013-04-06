import string
## from django.template import Context, loader
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.db.models import Q
import magiokis.songs.models as my
from magiokis.songs.getsongtekst import gettekst, updatetekst
## import sys
## sys.path.insert(0, '/home/albert/magiokis/data/songs')
## from songtekst import Songtekst

def index(request, melding=''): # klaar
    page_data = {"message": melding,
                "crumbs": [('/', 'Home', 'Magiokis'),
                            ('/songs/','start',"songs: start")]}
    page_data["title"] = "Start"
    if melding:
        page_data["message"] = melding
    return render_to_response('songs/index.html',page_data)

def songlist(request, melding='',soort='',data=''): # klaar
    page_data = {"message": melding,
                "crumbs": [('/', 'Home', 'Magiokis'),
                            ('/songs/','start',"songs: start"),
                            ('/songs/select/','select','select songs')]}
    page_data["title"] = "Select: songs "
    # kolom met letters opbouwen
    page_data['letterlijst'] = [x.letter for x in my.Letters.objects.all().order_by('letter')]
    #  kolom met jaren opbouwen
    page_data["jarenlijst"] = [x.jaar for x in my.Jaren.objects.all().order_by('jaar')]

    try:
        incoming = request.POST
    except:
        incoming = {}
    if 'select' in incoming:
        data = incoming['select']
        #-- zorgen dat 1-letter- of -cijferige titelselecties behandeld worden als letterselecties
        if soort == 'search':
            if data in list(string.punctuation):
                data = "("
                soort = "letter"
            elif data in list(string.digits):
                data = "0"
                soort = "letter"
            elif data in list(string.letters):
                soort = 'letter'
    if soort:
        page_data["crumbs"].append(('/songs/select/%s/%s/' % (soort,data),
            soort,'select songs by %s' % soort))

    #-- songlijst met songs (id, titel, xx, yy) en lijstoms
    if page_data["message"]:
        pass
    elif soort == "search":
        page_data["lijstoms"] = "met '%s' in titel" % data
        songslijst = my.Song.objects.filter(titel__icontains=data)
    elif soort == "letter":
        page_data["lijstoms"] = "met titel beginnend met letter '%s'" % data
        songslijst = my.Song.objects.filter(titel__istartswith=data)
    elif soort == "jaar":
        page_data["lijstoms"] = "uit jaar '%s'" % data
        songslijst = my.Song.objects.filter(Q(datering__startswith=data[2:])|
            Q(datering__contains="/"+data[2:]))
    elif not soort:
        pass
    else:
        page_data["message"] = "foute argumenten: soort=%s,data=%s" % (soort,data)

    if soort and not page_data["message"]:
        page_data["soort"] = soort
        page_data["title"] += page_data["lijstoms"]
        if songslijst.count() == 1:
            return HttpResponseRedirect("/songs/detail/{0}/".format(songslijst[0].id))
        page_data["songslijst"] = songslijst

    return render_to_response('songs/songlist.html',page_data)

def series(request, melding='',item=''): # klaar
    try:
        incoming = request.POST
        if 'select' in incoming:
            item = incoming['select']
    except:
        incoming = {}
    page_data = {"message": "",
                "crumbs": [('/', 'Home', 'Magiokis'),
                            ('/songs/','start',"songs: start"),
                            ("/songs/select/series/","select","select songserie")]}
    page_data["title"] = "Opnameseries"
    page_data["series"] = my.Songserie.objects.all().order_by('name')

    if item:
        data = my.Songserie.objects.get(pk=item)
        page_data["crumbs"].append(("/songs/select/series/{0}".format(item),'serie',
            'select song uit serie'))
        page_data["title"] = "Songs uit verzameling"
        page_data["serienaam"] = data.name
        page_data["songs"] = data.song.all()
        page_data["comment"] = data.comment
    return render_to_response('songs/series.html',page_data)

def detail(request, melding='',action='',item=""): # klaar
    try:
        incoming = request.POST
    except:
        incoming = {}
    page_data = {"message": "",
                "crumbs": [('/', 'Home', 'Magiokis'),
                            ('/songs/','start',"songs: start")]}
    page_data["title"] = "Detail"
    if item:
        page_data["crumbs"].append(('/songs/detail/%s/' % item,'detail','songs: song'))
        if action == "edit":
            page_data["crumbs"].append(('/songs/detail/%s/edit/' % item,'wijzig','songs: wijzig song'))
        song = my.Song.objects.get(pk=item)
        page_data["song"] = song
        opnames = []
        lijst = my.Opname.objects.filter(song=song.id).order_by('datum') # str(datum.naam))
        for item in lijst:
            it= {'id': item.id,
                'loc': ", ".join((item.plaats.naam,item.datum.naam)),
                'url': item.url.join(('','.mp3'))}
            if item.bezetting:
                oms = item.bezetting.naam
            else:
                oms = ", ".join([ins.naam for ins in item.instrumenten.all()])
            it['oms'] = "\n".join((oms,item.commentaar))
            opnames.append((item.datum.waarde,it))
        opnames.sort()
        page_data["opnames"] = [x[1] for x in opnames]
        registraties = my.Registratie.objects.filter(song=song.id).order_by('type')
        page_data["registraties"] = registraties
        tekst = song.url if song.url else song.titel + ".xml"
        ## y = ''
        try:
            x, y = gettekst(tekst)
        except TypeError:
            pass
        if y:
            page_data["tekst"] = [unicode(x), unicode(y)]
        ## ds = Songtekst(item)
        ## ds.read()
        ## page_data["tekst"] = (ds.titel, '<br />'.join(ds.regels))
        #~ return page_data
    elif action == "add":
        page_data["crumbs"].append(('/songs/detail/nieuw','nieuwe tekst','songs: nieuw'))
    else:
        melding = "Fout in aansturing: geen item of action (add)"

    if melding:
        page_data["message"] = melding
    if action:
        page_data["auteurs"] = my.Auteur.objects.all().order_by("naam")
        page_data["makers"] = my.Maker.objects.all().order_by("naam")
        return render_to_response('songs/wijzig.html',page_data)
    else:
        return render_to_response('songs/song.html',page_data)

def wijzigdetail(request, melding='',item=''): # klaar
    (r'^detail/(?P<item>\d+)/update/$',                            'wijzigdetail'),
    try:
        incoming = request.POST
    except:
        incoming = {}
    melding = ''
    titel = incoming.get("Titel",'')
    auteurval = incoming.get("Tekst",'')
    makerval = incoming.get("Muziek",'')
    datering = incoming.get("Datering",'')
    datumtekst = incoming.get("Datumtxt",'')
    opm = incoming.get("Opmerkingen",'')

    page_data = {"message": "",
                "crumbs": [('/', 'Home', 'Magiokis'),
                            ('/songs/','start',"songs: start")]}
    #~ if datering == '':
         #~ melding = "Wijzigen niet mogelijk: geen datering opgegeven"

    if not melding:
        if item:
            song = my.Song.objects.get(pk=item)
        else:
            song = my.Song.objects.create()
            item = song.id
        song.titel = titel
        # opgeven van nieuwe auteurs/makers zou ook mogelijk moeten zijn?
        song.tekst = my.Auteur.objects.get(pk=auteurval)
        song.muziek = my.Maker.objects.get(pk=makerval)
        song.datering = datering
        song.datumtekst = datumtekst
        song.commentaar = opm
        song.save()

    return HttpResponseRedirect('/songs/detail/{0}/'.format(item))

def wijzigtekst(request, melding='',action='', item=''):
    ## (r'^tekst/(?P<item>\d+)/(?P<action>(add|edit))/$',           'tekst'),
    ## (r'^tekst/(?P<item>\d+)/update/$',                           'wijzigtekst'),
    try:
        incoming = request.POST
    except:
        incoming = {}
    titel = incoming.get("titel",'')
    tekst = incoming.get("tekst",'')
    fnaam = incoming.get("fnaam",'')
    page_data = {"message": "",
                "crumbs": [('/', 'Home', 'Magiokis'),
                            ('/songs/','start',"songs: start")]}

    if not fnaam:
        song = my.Song.objects.get(pk=item)
        fnaam = song.url or song.titel + '.xml'
    if not action:
        updatetekst(fnaam, titel, tekst)
        page_data['message'] = 'Songtekst is aangepast'
    page_data['fnaam'] = page_data['fn'] = fnaam
    titel, tekst = gettekst(fnaam)
    ## return HttpResponse('{}: {}'.format(titel, tekst))
    page_data['titel'] = unicode(titel)
    page_data['tekst'] = unicode(tekst)
    page_data['id'] = item

    return render_to_response('songs/wijzigsongtekst.html', page_data)

def opnlist(request, melding='',item=""): # klaar
    try:
        incoming = request.POST
        if 'select' in incoming:
            item = incoming['select']
    except:
        incoming = {}
    page_data = {"message": "",
                "crumbs": [('/', 'Home', 'Magiokis'),
                            ('/songs/','start',"songs: start"),
                            ('songs/select/opnames/','select','select opnameserie')]}

    page_data["title"] = "Opnameseries"
    page_data["series"] = my.Opnameserie.objects.all().order_by('naam')
    if item:
        page_data["crumbs"].append((
            'songs/select/opnames/{0}'.format(item),'opname',
            'select opname uit serie'))
        data = my.Opnameserie.objects.get(id=item)
        page_data["title"] = "Opnames bij serie"
        page_data["serienaam"] = data.naam
        page_data["opnames"] = data.opname.all()
    return render_to_response('songs/opnlist.html',page_data)

def opname(request,melding='',item=''): # klaar
    try:
        incoming = request.POST
    except:
        incoming = {}
    page_data = {"message": "",
                "crumbs": [('/', 'Home', 'Magiokis'),
                            ('/songs/','start',"songs: start")]}
    page_data["title"] = "Detail Opname"
    #~ page_data["melding"] = item
    page_data["opn"] = my.Opname.objects.get(id=item)
    page_data["songs"] = my.Song.objects.all().order_by("titel")
    page_data["plaatsen"] = my.Plaats.objects.all().order_by("naam")
    page_data["datums"] = my.Datum.objects.all().order_by("naam")
    page_data["bezettingen"] = my.Bezetting.objects.all().order_by("naam")
    inslist = page_data["opn"].instrumenten.all().order_by("naam")
    allins = my.Instrument.objects.all().order_by("naam")
    page_data["opnins"] = [x for x in inslist]
    page_data["notins"] = [x for x in allins if x not in inslist]
    #~ return page_data
    return render_to_response('songs/opname.html',page_data)

def wijzigopname(request, melding='',item=''): # klaar
    try:
        incoming = request.POST
    except:
        incoming = {}
    song = incoming.get('Song','')
    plaats = incoming.get('Plaats','')
    datum = incoming.get('Datum','')
    bezetting = incoming.get('Bezet','')
    inslist = incoming.get('instcodes','')
    url = incoming.get('Url','')
    opm = incoming.get('Opm','')

    page_data = {"message": "",
                "crumbs": [('/', 'Home', 'Magiokis'),
                            ('/songs/','start',"songs: start")]}

    if url == '':
        melding = "Geen filenaam opgegeven"
    # je zou hier ook nieuwe plaatsen en datums moeten kunnen kiezen/opgeven

    if not melding:
        if item:
            opname = my.Opname.objects.get(pk=item)
        else:
            opname = my.Opname.objects.create()
            item = opname.id
        if song:
            opname.song = my.Song.objects.get(pk=song)
        if plaats:
            opname.plaats = my.Plaats.objects.get(pk=plaats)
        if datum:
            opname.datum = my.Datum.objects.get(pk=datum)
        if bezetting and bezetting != "0":
            opname.bezetting = my.Bezetting.objects.get(pk=bezetting)
        if inslist:
            inslist = inslist.split("$#$")
            opname.instrumenten.clear()
            for ins in inslist:
                opname.instrumenten.add(my.Instrument.objects.get(pk=ins))
        opname.url = url
        opname.commentaar = opm
        opname.save()

    return HttpResponseRedirect('/songs/opname/{0}/'.format(item))

def playopname(request,melding='',item=''):
    pass

def reglist(request, melding='',item=''): # klaar
    try:
        incoming = request.POST
    except:
        incoming = {}
    page_data = {"message": "",
                "crumbs": [('/', 'Home', 'Magiokis'),
                            ('/songs/','start',"songs: start")]}
    if item:
        naam = my.Regtype.objects.get(id=item).naam
        page_data["crumbs"].append((
            '/songs/select/regs/{0}/'.format(item),'select',
            'select regs van type'))
        page_data["serienaam"] = naam
        page_data["reglist"] = my.Registratie.objects.filter(type=item)
        page_data["doe"] =  "Bekijk" if item == "5" else "Play"
    return render_to_response('songs/reglist.html',page_data)

def reg(request='',melding='',item=''): # klaar
    try:
        incoming = request.POST
    except:
        incoming = {}
    page_data = {"message": "",
                "crumbs": [('/', 'Home', 'Magiokis'),
                            ('/songs/','start',"songs: start")]}
    page_data["title"] = "Detail registratie"
    page_data["reg"] = my.Registratie.objects.get(id=item)
    page_data["songs"] = my.Song.objects.all().order_by("titel")
    page_data["types"] = my.Regtype.objects.all()
    return render_to_response('songs/registratie.html',page_data)

def wijzigreg(request, melding='',item=''): # klaar
    try:
        incoming = request.POST
    except:
        incoming = {}
    song = incoming.get("Song","")
    soort = incoming.get("Soort","")
    url = incoming.get("Url","")
    opm = incoming.get("Opm","")

    page_data = {"message": "",
                "crumbs": [('/', 'Home', 'Magiokis'),
                            ('/songs/','start',"songs: start")]}
    if not melding:
        if item:
            reg = my.Registratie.objects.get(pk=item)
        else:
            reg = my.Registratie.objects.create()
            item = reg.id
        if song:
            reg.song = my.Song.objects.get(pk=song)
        if soort:
            reg.type = my.Regtype.objects.get(pk=soort)
        reg.url = url
        reg.commentaar = opm
        reg.save()

    return HttpResponseRedirect('/songs/reg/{0}/'.format(item))

def playreg(request,melding='',item=''):
    pass
def tabel(request, melding='',soort=''): # klaar
    try:
        incoming = request.POST
    except:
        incoming = {}
    page_data = {"message": "",
                "crumbs": [('/', 'Home', 'Magiokis'),
                            ('/songs/','start',"songs: start")]}
    if soort:
        page_data["crumbs"].append(("/songs/tabel/{0}/".format(soort),
            'tabel','toon/wijzig tabel'))
        page_data["title"] = "Tabellenbeheer: " + soort
        page_data["tabsoort"] = soort
        if soort == "Auteur":
            data = my.Auteur.objects.all().order_by("naam")
        elif soort == "Maker":
            data = my.Maker.objects.all().order_by("naam")
        elif soort == "Datum":
            data = my.Datum.objects.all().order_by("naam")
            page_data["tabwrd"] = "Sorteerwaarde"
        elif soort == "Plaats":
            data = my.Plaats.objects.all().order_by("naam")
        elif soort == "Bezetting":
            data = my.Bezetting.objects.all().order_by("naam")
        elif soort == "Instrument":
            data = my.Instrument.objects.all().order_by("naam")
        elif soort == "Regtype":
            data = my.Regtype.objects.all().order_by("naam")
        page_data["tabel"] = data
    if soort == "Regtype":
        return render_to_response('songs/regtype.html',page_data)
    else:
        return render_to_response('songs/tabel.html',page_data)

def wijzigtabel(request, melding='',soort='',item=''): # klaar
    try:
        incoming = request.POST
    except:
        incoming = {}
    naam = incoming.get("txtNaam",'')
    if soort == 'Regtype':
        pad = incoming.get("txtPad",'')
        htmlpad = incoming.get("txtHTMLPad",'')
        player = incoming.get("txtPlayer",'')
        editor = incoming.get("txtEditor",'')
    else:
        waarde = incoming.get("txtWaarde",'')
    #~ return HttpResponse("<br/>".join(incoming.values()))
    page_data = {"message": "",
                "crumbs": [('/', 'Home', 'Magiokis'),
                            ('/songs/','start',"songs: start")]}

    if soort == "Auteur":
        if item:
            data = my.Auteur.objects.get(pk=item)
        else:
            data = my.Auteur.objects.create()
    elif soort == "Maker":
        if item:
            data = my.Maker.objects.get(pk=item)
        else:
            data = my.Maker.objects.create()
    elif soort == "Plaats":
        if item:
            data = my.Plaats.objects.get(pk=item)
        else:
            data = my.Plaats.objects.create()
    elif soort == "Datum":
        if item:
            data = my.Datum.objects.get(pk=item)
        else:
            data = my.Datum.objects.create()
            item = data.id
    elif soort == "Bezetting":
        if item:
            data = my.Bezetting.objects.get(pk=item)
        else:
            data = my.Bezetting.objects.create()
    elif soort == "Instrument":
        if item:
            data = my.Instrument.objects.get(pk=item)
        else:
            data = my.Instrument.objects.create()
    elif soort == 'Regtype':
        if item:
            data = my.Regtype.objects.get(pk=item)
        else:
            data = my.Regtype.objects.create()
    if not item:
        item = data.id

    data.naam = naam
    if soort == 'Regtype':
        data.pad = pad
        data.htmlpad = htmlpad
        data.player = player
        data.editor = editor
    elif soort == "Datum":
        data.waarde = waarde
    data.save()

    return HttpResponseRedirect('/songs/tabel/{0}/'.format(soort))
