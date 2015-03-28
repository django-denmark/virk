from django.db import models

# Create your models here.


class Firma(models.Model):
    cvrnr = models.CharField(max_length=10, unique=True, primary_key=True)
    ajourfoeringsdato = models.DateField()
    reklamebeskyttelse = models.BooleanField(default=True)

    def __unicode__(self):
        return self.cvrnr


class Navn(models.Model):
    firma = models.ForeignKey(Firma, related_name='navne')
    gyldigFra = models.DateField(blank=True, null=True)
    gyldigTil = models.DateField(blank=True, null=True)
    tekst = models.CharField(max_length=300)


class Beliggenhedsadresse(models.Model):
    firma = models.ForeignKey(Firma, related_name='addresser')
    gyldigFra = models.DateField(blank=True, null=True)
    gyldigTil = models.DateField(blank=True, null=True)
    vejnavn = models.CharField(max_length=100, blank=True, null=True)
    vejkode = models.CharField(max_length=20, blank=True, null=True)
    husnummerFra = models.CharField(max_length=10, blank=True, null=True)
    husnummerTil = models.CharField(max_length=10, blank=True, null=True)
    bogstavFra = models.CharField(max_length=5, blank=True, null=True)
    bogstavTil = models.CharField(max_length=5, blank=True, null=True)
    etage = models.CharField(max_length=10, blank=True, null=True)
    sidedoer = models.CharField(max_length=10, blank=True, null=True)
    postnr = models.CharField(max_length=10, blank=True, null=True)
    postdistrikt = models.CharField(max_length=50, blank=True, null=True)
    bynavn = models.CharField(max_length=50, blank=True, null=True)
    kommune_kode = models.CharField(max_length=10, blank=True, null=True)
    kommune_tekst = models.CharField(max_length=50, blank=True, null=True)
    postboks = models.CharField(max_length=50, blank=True, null=True)
    adresseFritekst = models.CharField(max_length=100, blank=True, null=True)


class Virksomhedsform(models.Model):
    firma = models.ForeignKey(Firma, related_name='virksomhedsform')
    gyldigFra = models.DateField()
    gyldigTil = models.DateField(blank=True, null=True)
    kode = models.CharField(max_length=10, blank=True, null=True)
    tekst = models.CharField(max_length=90, blank=True, null=True)
    ansvarligDataleverandoer = models.CharField(max_length=50)


class HovedBranche(models.Model):
    firma = models.ForeignKey(Firma, related_name='hovedbranche')
    gyldigFra = models.DateField(blank=True, null=True)
    gyldigTil = models.DateField(blank=True, null=True)
    kode = models.CharField(max_length=10, blank=True, null=True)
    tekst = models.CharField(max_length=150, blank=True, null=True)


class Produktionsenheder(models.Model):
    firma = models.ForeignKey(Firma, related_name='produktionsenheder')
    gyldigFra = models.DateField()
    gyldigTil = models.DateField(blank=True, null=True)
    pnr = models.CharField(max_length=10, blank=True)


class Livsforloeb(models.Model):
    firma = models.ForeignKey(Firma, related_name='livsforloeb')
    startdato = models.DateField(blank=True, null=True)
    ophoersdato = models.DateField(blank=True, null=True)
