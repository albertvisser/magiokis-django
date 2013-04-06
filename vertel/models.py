from django.db import models
import datetime

class Verteller(models.Model):
    voornaam = models.CharField(max_length=20,blank=True)
    achternaam = models.CharField(max_length=40,blank=True)
    pseudoniem = models.CharField(max_length=40,blank=True)
    def __unicode__(self):
        if self.pseudoniem:
            return self.pseudoniem
        else:
            return ' '.join((self.voornaam,self.achternaam))
    class Admin:
        pass

class Verhaal(models.Model):
    titel = models.CharField(max_length=100)
    schrijver = models.ForeignKey(Verteller)
    datum_begonnen = models.DateTimeField('Begonnen op',auto_now_add=True)
    datum_afgemaakt = models.DateTimeField('Afgemaakt op',null=True,blank=True)
    def __unicode__(self):
        return self.titel
    ## class Admin:
        ## fields = (
            ## (None, {'fields': ('question',)}),
            ## ('Date information', {'fields': ('pub_date',), 'classes': 'collapse'}),
        ## )
        ## list_display = ('question', 'pub_date', 'was_published_today')
        ## list_filter = ['pub_date']
        ## search_fields = ['question']
        ## date_hierarchy = 'pub_date'
    class Admin:
        pass

class Hoofdstuk(models.Model):
    verhaal = models.ForeignKey(Verhaal,related_name='hoofdstukken')
    titel = models.CharField(max_length=100)
    inhoud = models.TextField()
    def __unicode__(self):
        return self.titel
    class Admin:
        pass

class Bundel(models.Model):
    titel = models.CharField(max_length=40)
    beschrijving = models.TextField(blank=True)
    inhoud = models.ManyToManyField(Verhaal,related_name='bundel')
    def __unicode__(self):
        return self.titel
    class Admin:
        pass
