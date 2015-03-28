from django.contrib import admin
from .models import (
    Firma, Navn, Beliggenhedsadresse, Virksomhedsform, HovedBranche
)


class NavnInline(admin.TabularInline):
    model = Navn

class BeliggenhedsadresseInline(admin.TabularInline):
    model = Beliggenhedsadresse

class VirksomhedsformInline(admin.TabularInline):
    model = Virksomhedsform

class HovedBrancheInline(admin.TabularInline):
    model = HovedBranche


class FirmatAdmin(admin.ModelAdmin):
    raw_id_fields = []
    inlines = [
        BeliggenhedsadresseInline,
        VirksomhedsformInline,
        HovedBrancheInline,
    ]

admin.site.register(Firma, FirmatAdmin)
