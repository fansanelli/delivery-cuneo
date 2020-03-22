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


CATEGORIES_MAP = {
    'ALIMENTARI': [ 'shop=convenience', 'shop=general' ],
    'BAR': [ 'amenity=cafe', 'amenity=bar' ],
}


def main():
    if which('osmfilter') is None:
        print('osmfilter not found')
        sys.exit(0)

    for key, value in CATEGORIES_MAP.items():
        f = open(key + '.osm', 'w')
        keep = ' or '.join(value)
        subprocess.run(['osmfilter', './delivery.osm', '--keep=' + keep], stdout=f)
        f.close()

    drop = ' and '.join(CATEGORIES_MAP['ALIMENTARI'] + CATEGORIES_MAP['BAR'])
    f = open('ALTRI.osm', 'w')
    subprocess.run(['osmfilter', './delivery.osm', '--drop=' + drop], stdout=f)


if __name__ == "__main__":
    main()
