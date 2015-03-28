# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beliggenhedsadresse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gyldigFra', models.DateField(null=True, blank=True)),
                ('gyldigTil', models.DateField(null=True, blank=True)),
                ('vejnavn', models.CharField(max_length=100, null=True, blank=True)),
                ('vejkode', models.CharField(max_length=20, null=True, blank=True)),
                ('husnummerFra', models.CharField(max_length=10, null=True, blank=True)),
                ('husnummerTil', models.CharField(max_length=10, null=True, blank=True)),
                ('bogstavFra', models.CharField(max_length=5, null=True, blank=True)),
                ('bogstavTil', models.CharField(max_length=5, null=True, blank=True)),
                ('etage', models.CharField(max_length=10, null=True, blank=True)),
                ('sidedoer', models.CharField(max_length=10, null=True, blank=True)),
                ('postnr', models.CharField(max_length=10, null=True, blank=True)),
                ('postdistrikt', models.CharField(max_length=50, null=True, blank=True)),
                ('bynavn', models.CharField(max_length=50, null=True, blank=True)),
                ('kommune_kode', models.CharField(max_length=10, null=True, blank=True)),
                ('kommune_tekst', models.CharField(max_length=50, null=True, blank=True)),
                ('postboks', models.CharField(max_length=50, null=True, blank=True)),
                ('adresseFritekst', models.CharField(max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Firma',
            fields=[
                ('cvrnr', models.CharField(max_length=10, unique=True, serialize=False, primary_key=True)),
                ('ajourfoeringsdato', models.DateField()),
                ('reklamebeskyttelse', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='HovedBranche',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gyldigFra', models.DateField(null=True, blank=True)),
                ('gyldigTil', models.DateField(null=True, blank=True)),
                ('kode', models.CharField(max_length=10, null=True, blank=True)),
                ('tekst', models.CharField(max_length=150, null=True, blank=True)),
                ('firma', models.ForeignKey(related_name='hovedbranche', to='cvr.Firma')),
            ],
        ),
        migrations.CreateModel(
            name='Livsforloeb',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('startdato', models.DateField(null=True, blank=True)),
                ('ophoersdato', models.DateField(null=True, blank=True)),
                ('firma', models.ForeignKey(related_name='livsforloeb', to='cvr.Firma')),
            ],
        ),
        migrations.CreateModel(
            name='Navn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gyldigFra', models.DateField(null=True, blank=True)),
                ('gyldigTil', models.DateField(null=True, blank=True)),
                ('tekst', models.CharField(max_length=300)),
                ('firma', models.ForeignKey(related_name='navne', to='cvr.Firma')),
            ],
        ),
        migrations.CreateModel(
            name='Produktionsenheder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gyldigFra', models.DateField()),
                ('gyldigTil', models.DateField(null=True, blank=True)),
                ('pnr', models.CharField(max_length=10, blank=True)),
                ('firma', models.ForeignKey(related_name='produktionsenheder', to='cvr.Firma')),
            ],
        ),
        migrations.CreateModel(
            name='Virksomhedsform',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gyldigFra', models.DateField()),
                ('gyldigTil', models.DateField(null=True, blank=True)),
                ('kode', models.CharField(max_length=10, null=True, blank=True)),
                ('tekst', models.CharField(max_length=90, null=True, blank=True)),
                ('ansvarligDataleverandoer', models.CharField(max_length=50)),
                ('firma', models.ForeignKey(related_name='virksomhedsform', to='cvr.Firma')),
            ],
        ),
        migrations.AddField(
            model_name='beliggenhedsadresse',
            name='firma',
            field=models.ForeignKey(related_name='addresser', to='cvr.Firma'),
        ),
    ]
