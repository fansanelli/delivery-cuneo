#!/usr/bin/env python

###########################################################################
##                                                                       ##
## Copyrights Francesco Ansanelli 2020                                   ##
##                                                                       ##
## This program is free software: you can redistribute it and/or modify  ##
## it under the terms of the GNU General Public License as published by  ##
## the Free Software Foundation, either version 3 of the License, or     ##
## (at your option) any later version.                                   ##
##                                                                       ##
## This program is distributed in the hope that it will be useful,       ##
## but WITHOUT ANY WARRANTY; without even the implied warranty of        ##
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         ##
## GNU General Public License for more details.                          ##
##                                                                       ##
## You should have received a copy of the GNU General Public License     ##
## along with this program.  If not, see <http://www.gnu.org/licenses/>. ##
##                                                                       ##
###########################################################################

from shutil import which
import sys
import subprocess
import os


CATEGORIES_MAP = {
    'ABBIGLIAMENTO': [ 'shop=clothes', 'shop=shoes' ],
    'ALIMENTARI': [ 'shop=convenience', 'shop=deli', 'shop=frozen_food', 'shop=general', 'shop=health_food', 'shop=pasta', 'shop=seafood', 'shop=supermarket' ],
    'ANIMALI': [ 'shop=pet' ],
    'BAR': [ 'amenity=cafe', 'amenity=bar', 'shop=wine' ],
    'CIBO': [ 'amenity=fast_food', 'amenity=pub', 'amenity=restaurant' ],
    'COMPUTER_ELETTRONICA': [ 'shop=appliance', 'shop=electronics', 'shop=ink', 'shop=printer_ink' ],
    'DOLCI': [ 'shop=confectionery', 'shop=pastry' ],
    'FIORI': [ 'shop=florist', 'shop=garden_centre' ],
    'LATTE_DERIVATI': [ 'amenity=ice_cream', 'shop=cheese', 'shop=dairy', 'shop=ice_cream' ],
    'MACELLERIE': [ 'shop=butcher' ],
    'ORTOFRUTTA': [ 'shop=farm', 'shop=greengrocer' ],
    'PANETTERIE': [ 'shop=bakery' ],
    'SALUTE': [ 'amenity=pharmacy', 'shop=hearing_aids', 'shop=herbalist', 'shop=medical_supply' ]
}


def main():
    if which('osmfilter') is None:
        print('osmfilter not found')
        sys.exit(0)

    if which('osmconvert') is None:
        print('osmconvert not found')
        sys.exit(0)

    # calcola il centroide delle way
    subprocess.run(['osmconvert', './delivery.osm', '--all-to-nodes', '-o=./tmp_delivery.osm'])

    for key, value in CATEGORIES_MAP.items():
        f = open('extracted/' + key + '.osm', 'w')
        keep = ' or '.join(value)
        subprocess.run(['osmfilter', './tmp_delivery.osm', '--keep=' + keep], stdout=f)
        f.close()

    drop = ' or '.join(CATEGORIES_MAP['ABBIGLIAMENTO']
        + CATEGORIES_MAP['ALIMENTARI']
        + CATEGORIES_MAP['ANIMALI']
        + CATEGORIES_MAP['BAR']
        + CATEGORIES_MAP['CIBO']
        + CATEGORIES_MAP['COMPUTER_ELETTRONICA']
        + CATEGORIES_MAP['DOLCI']
        + CATEGORIES_MAP['FIORI']
        + CATEGORIES_MAP['LATTE_DERIVATI']
        + CATEGORIES_MAP['MACELLERIE']
        + CATEGORIES_MAP['ORTOFRUTTA']
        + CATEGORIES_MAP['PANETTERIE']
        + CATEGORIES_MAP['SALUTE'])
    f = open('extracted/ALTRI.osm', 'w')
    # keep=* rimuove i nodi vuoti
    subprocess.run(['osmfilter', './tmp_delivery.osm', '--keep=*', '--drop=' + drop], stdout=f)

    os.remove("./tmp_delivery.osm")


if __name__ == "__main__":
    main()
