from django.db import models

class Auteur(models.Model):
    naam = models.CharField(max_length=80,blank=True)
    class Meta:
        db_table = u'auteurs'
    def __unicode__(self):
        return self.naam

class Maker(models.Model):
    naam = models.CharField(max_length=80,blank=True)
    class Meta:
        db_table = u'makers'
    def __unicode__(self):
        return self.naam

class Datum(models.Model):
    naam = models.CharField(max_length=80,blank=True)
    waarde = models.IntegerField(blank=True)
    class Meta:
        db_table = u'datums'
    def __unicode__(self):
        return self.naam

class Plaats(models.Model):
    naam = models.CharField(max_length=80,blank=True)
    class Meta:
        db_table = u'plaatsen'
    def __unicode__(self):
        return self.naam

class Bezetting(models.Model):
    naam = models.CharField(max_length=120,blank=True)
    class Meta:
        db_table = u'bezettingen'
    def __unicode__(self):
        return self.naam

class Instrument(models.Model):
    naam = models.CharField(max_length=80,blank=True)
    class Meta:
        db_table = u'instrumenten'
    def __unicode__(self):
        return self.naam

class Song(models.Model):
    muziek = models.ForeignKey(Maker,blank=True,null=True)
    tekst = models.ForeignKey(Auteur,blank=True,null=True)
    titel = models.CharField(max_length=80,blank=True)
    datering = models.CharField(max_length=40,blank=True)
    datumtekst = models.CharField(max_length=60,blank=True)
    url = models.CharField(max_length=80,blank=True)
    commentaar = models.TextField(blank=True)
    class Meta:
        db_table = u'songs'
    def __unicode__(self):
        return self.titel

class Serieitem(models.Model):
    song = models.ForeignKey(Song)
    comment = models.TextField(blank=True)
    class Meta:
        db_table = u'serieitems'
    def __unicode__(self):
        return str(self.song)
    
class Songserie(models.Model):
    name = models.CharField(max_length=60,blank=True)
    song = models.ManyToManyField(Serieitem,related_name="serie")
    comment = models.TextField(blank=True)
    class Meta:
        db_table = u'songseries'
    def __unicode__(self):
        return self.name

class Jaren(models.Model):
    jaar = models.CharField(max_length=4,primary_key=True)
    song = models.ManyToManyField(Serieitem,related_name="jaar")
    tekst = models.TextField(blank=True)
    class Meta:
        db_table = u'jaren'
    def __unicode__(self):
        return self.jaar

class Letters(models.Model):
    letter = models.CharField(max_length=1,primary_key=True)
    song = models.ManyToManyField(Serieitem,related_name="beginletter")
    tekst = models.TextField(blank=True)
    class Meta:
        db_table = u'letters'
    def __unicode__(self):
        return self.letter

class Opname(models.Model):
    plaats = models.ForeignKey(Plaats,blank=True,null=True)
    datum = models.ForeignKey(Datum,blank=True,null=True)
    song = models.ForeignKey(Song,null=True)
    bezetting = models.ForeignKey(Bezetting,blank=True,null=True)
    instrumenten = models.ManyToManyField(Instrument,blank=True,null=True)
    url = models.CharField(max_length=80)
    commentaar = models.TextField(blank=True)
    class Meta:
        db_table = u'opnames'
    def __unicode__(self):
        return self.url

class Opnameserie(models.Model):
    naam = models.CharField(max_length=20,blank=True)
    titel = models.CharField(max_length=60,blank=True)
    opname = models.ManyToManyField(Opname,blank=True)
    opgenomen = models.CharField(max_length=60,blank=True)
    class Meta:
        db_table = u'opnameseries'
    def __unicode__(self):
        return self.naam

class Regtype(models.Model):
    naam = models.CharField(max_length=20,blank=True)
    pad = models.CharField(max_length=40,blank=True)
    htmlpad = models.CharField(max_length=40,blank=True)
    player = models.CharField(max_length=60,blank=True)
    editor = models.CharField(max_length=60,blank=True)
    class Meta:
        db_table = u'regtypes'
    def __unicode__(self):
        return self.naam

class Registratie(models.Model):
    type = models.ForeignKey(Regtype)
    song = models.ForeignKey(Song,null=True)
    url = models.CharField(max_length=80,blank=True)
    commentaar = models.TextField(blank=True)
    class Meta:
        db_table = u'registraties'
    def __unicode__(self):
        return ": ".join((str(self.type),self.url))
