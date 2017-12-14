#!/usr/bin/env python

import os

katalog="."
for nazwaKatalogu,listaKatalogow,listaPlikow in os.walk(katalog):
    print ("Folder :"+nazwaKatalogu)
    for nazwa in listaPlikow:
        print ('\t' +nazwa)
