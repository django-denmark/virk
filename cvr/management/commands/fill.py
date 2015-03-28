from django.core.management.base import BaseCommand
import xmltodict
import json


class Command(BaseCommand):

    def handle(self, *args, **options):

        def do_magic(_, dct):
            print "oop"

        def fill_from_xml():
            with open('output_privat.xml') as fh:
                xmltodict.parse(fh, item_depth=3, item_callback=do_magic)

        with open('cvr.json') as fh:
            lst = json.load(fh)
            [do_magic(None, x) for x in lst]
