from django.db import models

# Create your models here.

class Trefw(models.Model):
    woord = models.CharField(max_length=30)
    def __str__(self):
        return self.woord
    class Admin:
        pass

class Denksel(models.Model):
    titel = models.CharField(max_length=80)
    tekst = models.TextField(blank=True)
    trefwoorden = models.ManyToManyField(Trefw,related_name='teksten')
    def __str__(self):
        return self.titel
    class Admin:
        pass
