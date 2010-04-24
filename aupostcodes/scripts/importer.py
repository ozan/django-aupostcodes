#!/usr/bin/env python
"""
Import postal area data from the Australia Post csv of same.

At time of writing, this was available at 
http://auspost.com.au/static/docs/pc-full_20100330.csv
or from http://auspost.com.au/apps/postcode.html.
"""
import csv
import sys
import os

sys.path.append(os.path.abspath('../..'))

from django.core.management import setup_environ
from project import settings

setup_environ(settings)

from project.aupostcodes.models import AUPostalArea, AUPostCode


def create_postcodes(filepath):
    reader = csv.reader(open(filepath, 'U'))
    reader.next() # skip headers
    for line in reader:
        postcode, locality, state = line[:3]
        au_postcode, created = AUPostCode.objects.get_or_create(postcode=postcode)
        au_postal_area = AUPostalArea(postcode=au_postcode, locality=locality, state=state)
        au_postal_area.save()        
        
if __name__ == '__main__':
    filepath = os.path.abspath('data/pc-full_20100330.csv')
    create_postcodes(filepath)
    
    