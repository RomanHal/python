#!/usr/bin/env python
#-*-coding: utf-8
print ("plik do przetworzenia")
nazwa=raw_input()
plik=open(nazwa)

tresc= plik.read()
plik.close()
tresc=tresc.replace("się", "")
print tresc
tresc=tresc.replace("i", "")
print tresc
tresc=tresc.replace("oraz", "")
tresc=tresc.replace("nigdy", "")
tresc=tresc.replace("dlaczego", "")
plik=open(nazwa,'w')
plik.write(tresc)
plik.close()
