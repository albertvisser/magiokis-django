"""Data object definities voor Songs database
"""
import os
from django.db import models


class Auteur(models.Model):
    "lyricist"
    naam = models.CharField(max_length=80, blank=True)

    class Meta:
        db_table = 'auteurs'

    def __str__(self):
        return self.naam


class Maker(models.Model):
    "composer"
    naam = models.CharField(max_length=80, blank=True)

    class Meta:
        db_table = 'makers'

    def __str__(self):
        return self.naam


class Datum(models.Model):
    "recording date"
    naam = models.CharField(max_length=80, blank=True)
    waarde = models.IntegerField(blank=True)

    class Meta:
        db_table = 'datums'

    def __str__(self):
        return self.naam


class Plaats(models.Model):
    "recording location"
    naam = models.CharField(max_length=80, blank=True)

    class Meta:
        db_table = 'plaatsen'

    def __str__(self):
        return self.naam


class Bezetting(models.Model):
    "personnel"
    naam = models.CharField(max_length=120, blank=True)

    class Meta:
        db_table = 'bezettingen'

    def __str__(self):
        return self.naam


class Instrument(models.Model):
    "instrument used"
    naam = models.CharField(max_length=80, blank=True)

    class Meta:
        db_table = 'instrumenten'

    def __str__(self):
        return self.naam


class Song(models.Model):
    "song"
    muziek = models.ForeignKey(Maker, blank=True, null=True)
    tekst = models.ForeignKey(Auteur, blank=True, null=True)
    titel = models.CharField(max_length=80, blank=True)
    datering = models.CharField(max_length=40, blank=True)
    datumtekst = models.CharField(max_length=60, blank=True)
    url = models.CharField(max_length=80, blank=True)
    commentaar = models.TextField(blank=True)

    class Meta:
        db_table = 'songs'

    def __str__(self):
        return self.titel


class Serieitem(models.Model):
    "song as item in collection"
    song = models.ForeignKey(Song)
    comment = models.TextField(blank=True)

    class Meta:
        db_table = 'serieitems'

    def __str__(self):
        return str(self.song)


class Songserie(models.Model):
    "song collection"
    name = models.CharField(max_length=60, blank=True)
    song = models.ManyToManyField(Serieitem, related_name="serie")
    comment = models.TextField(blank=True)

    class Meta:
        db_table = 'songseries'

    def __str__(self):
        return self.name


class Jaren(models.Model):
    "year written as song collection"
    jaar = models.CharField(max_length=4, primary_key=True)
    song = models.ManyToManyField(Serieitem, related_name="jaar")
    tekst = models.TextField(blank=True)

    class Meta:
        db_table = 'jaren'

    def __str__(self):
        return self.jaar


class Letters(models.Model):
    "first letter of name as song collection"
    letter = models.CharField(max_length=1, primary_key=True)
    song = models.ManyToManyField(Serieitem, related_name="beginletter")
    tekst = models.TextField(blank=True)

    class Meta:
        db_table = 'letters'

    def __str__(self):
        return self.letter


class Opname(models.Model):
    "song recording"
    plaats = models.ForeignKey(Plaats, blank=True, null=True)
    datum = models.ForeignKey(Datum, blank=True, null=True)
    song = models.ForeignKey(Song, null=True)
    bezetting = models.ForeignKey(Bezetting, blank=True, null=True)
    instrumenten = models.ManyToManyField(Instrument, blank=True)
    url = models.CharField(max_length=80)
    commentaar = models.TextField(blank=True)

    class Meta:
        db_table = 'opnames'

    def __str__(self):
        return self.url


class Opnameserie(models.Model):
    "collection of song recordings"
    naam = models.CharField(max_length=20, blank=True)
    titel = models.CharField(max_length=60, blank=True)
    opname = models.ManyToManyField(Opname, blank=True)
    opgenomen = models.CharField(max_length=60, blank=True)

    class Meta:
        db_table = 'opnameseries'

    def __str__(self):
        return self.naam


class Regtype(models.Model):
    "registration type"
    naam = models.CharField(max_length=20, blank=True)
    pad = models.CharField(max_length=40, blank=True)
    htmlpad = models.CharField(max_length=40, blank=True)
    player = models.CharField(max_length=60, blank=True)
    editor = models.CharField(max_length=60, blank=True)

    class Meta:
        db_table = 'regtypes'

    def __str__(self):
        return self.naam


class Registratie(models.Model):
    "registration of song"
    type = models.ForeignKey(Regtype)
    song = models.ForeignKey(Song, null=True)
    url = models.CharField(max_length=80, blank=True)
    commentaar = models.TextField(blank=True)

    class Meta:
        db_table = 'registraties'

    def __str__(self):
        return ": ".join((str(self.type), self.url))

    def play(self):
        if self.type == '5':
            return 'mmap'
        result = os.path.splitext(self.url)[1][1:].lower()
        if self.type == '7':
            result += '/oud'
        return result
