import sqlite3 as sql
## inserten toch maar m.b.v. Django-API ##

def get_dic(series,cur):
    dic = {}
    for serie in series:
        dic[serie] = []
    for row in cur:
        dic[row[0]].append(row[1:])
    return dic

class Copyover(object):
    def __init__(self):
        dbnaam = "/home/visser/django/pythoneer/songs/songs.db"
        self.con = sql.connect(dbnaam)
        #~ destdb = "/home/visser/django/pythoneer/magiokis.db"
        #~ self.con2 = sql.connect(destdb)
        
    def tabellen(self):
        """
        leest de codetabellen
        auteurs, makers, datum, plaatsen, bezettingen en instrumenten
        en zet de gegevens in een lijst
        deze lijsten komen als waarde in een dictionary met de tabel als
        sleutel
        #! bij het opvoeren van deze tabellen is het wellicht handig om 
        #! voor het omgekeerd opzoeken een dictionary op te bouwen van
        #! naam - rowid paren
        """
        cur = self.con.cursor()
        data = {}
        for tabnaam in ("auteurs","makers","datums","plaatsen","bezettingen",
            "instrumenten"):
            cur.execute("SELECT * FROM " + tabnaam)
            newid = 1
            data[tabnaam] = [row[1:] for row in cur]
        self.con.commit()
        return data

    def regtypes(self):
        """
        leest de regtypes tabel en zet de gegevens in een lijst
        #! bij het opvoeren van deze tabel is het wellicht handig om 
        #! voor het omgekeerd opzoeken een dictionary op te bouwen van
        #! naam - rowid paren
        """
        cur = self.con.cursor()
        cur.execute("select * from regtypes")
        return [row for row in cur]

    def muziekreg(self):
        """
        leest de registraties tabel en bouwt een lijst op met alle gerelateerde
        gegevens in tekstvorm
        """
        cur = self.con.cursor()
        cur.execute('select '
            'registraties.url, registraties.commentaar, '
            'regtypes.naam, songs.titel '
            'from registraties,songs,regtypes '
            'where songs.id == registraties.song '
            'and regtypes.id == registraties.type')
        return [row for row in cur]
      
    def songtekst(self,naam):
        #~ read/write (nog) met elementtree
        cur = self.con.cursor()
        cur.execute()

    def song(self,naam=""):
        """
        leest de songs tabel en bouwt een lijst op met alle gerelateerde gegevens
        in tekstvorm
        #! bij het opvoeren van deze tabellen is het wellicht handig om 
        #! voor het omgekeerd opzoeken een dictionary op te bouwen van
        #! naam - rowid paren
        """
        cur = self.con.cursor()
        cur.execute('select '
            'songs.titel, auteurs.naam, makers.naam, songs.datering, '
            'songs.datumtekst, songs.url, songs.commentaar '
            'from songs '
            'left outer join auteurs on auteurs.id == songs.tekst '
            'left outer join makers on makers.id == songs.muziek')
        return [row for row in cur]
        
    def opname(self,naam=""):
        """
        leest de tabellen opnameseries en opnames en bouwt per opnameserie
        een lijst op van opnames met alle gerelateerde gegevens in tekstvorm
        deze lijsten komen als waarde in een dictionary met de opnameserie
        als sleutel
        """
        cur = self.con.cursor()
        cur.execute('select * from opnameseries where opname == ""')
        data = {}
        for row in cur:
            data[row[0]] = (row[1:],[])
        for id,serie in data.items():
            cur.execute('select * from opnameseries '
                'where opname != "" and id == ?',(id,))
            for row in cur:
                serie[1].append(row[1])
        cur.execute('select opnames.id, '
            'plaatsen.naam, datums.naam, songs.titel, bezettingen.naam, '
            'opnames.instrumenten, opnames.url, opnames.commentaar '
            'from opnames '
            'left outer join plaatsen on plaatsen.id == opnames.plaats '
            'left outer join datums on datums.id == opnames.datum '
            'left outer join songs on songs.id == opnames.song '
            'left outer join bezettingen on bezettingen.id == opnames.bezetting')
        songs = [row for row in cur]
        cur.execute('select * from instrumenten')
        instr = dict([row for row in cur])
        opn = {}
        for id, plaats, datum, song, bezetting, inslist, url, commentaar in songs:
            thing = []
            if inslist:
                for ins in inslist:
                    try:
                        thing.append(instr[ins])
                    except KeyError:
                        pass
            opn[id] = [plaats, datum, song, bezetting, thing, url, commentaar]
        for key in data:
            item, opnids = data[key]
            opns = [opn[id] for id in opnids]
            data[key] = (item, opns)
        return data

    def songlist(self):
        """
        leest de volgende tabellen met lijsten van songs:
        series, letters, jaren
        en zet de titels van de songs in elke lijst weg als waarde
        in een dictionary met de lijstaanduiding (welke serie, letter of jaar)
        als sleutel; en de verzamelingen lijstaanduidingen van hetzelfde type
        staan weer als waarde in een dictionary met de type lijstaanduiding
        als sleutel.
        Daarnaast wordt een lijst opgebouwd met per lijstaanduiding een 
        eventuele omschrijving.
        """
        data = {'series': [], 'letters': [], 'jaren': []}
        more_data = []
        cur = self.con.cursor()
        cur.execute('select distinct id from songseries')
        series = [row[0] for row in cur]
        cur.execute('select * from songseries')
        data['series'] = get_dic(series,cur)
        cur.execute('select id,tekst from letters where song == ""')
        series = [row for row in cur]
        more_data.append([(x,y) for x,y in series])
        series = [x[0] for x in series]
        cur.execute('select * from letters where song != ""')
        data['letters'] = get_dic(series,cur)
        cur.execute('select id, tekst from jaren where song == ""')
        series = [row for row in cur]
        more_data.append([(x,y) for x,y in series])
        series = [x[0] for x in series]
        cur.execute('select * from jaren where song != ""')
        data['jaren'] = get_dic(series,cur)
        cur.execute('select id,titel from songs')
        songdict = dict([row for row in cur])
        for item in data:
            for key,songlist in data[item].items():
                newlist = [(songdict[song],comment)
                    for song,comment in songlist]
                data[item][key] = newlist
        return data, more_data
        
if __name__ == "__main__":
    test = Copyover()
    #~ t = test.tabellen()
    #~ for x,y in t.items():
        #~ print x.join(('--- ',' ---'))
        #~ print y
    t = test.songlist()
    for x in t:
        print x