#!/usr/bin/env python

print ("plik do przetworzenia")
nazwa=raw_input()
plik=open(nazwa)

tresc= plik.read()
plik.close()
tresc=tresc.replace("i", "%temp%")

tresc=tresc.replace("oraz", "i")
tresc=tresc.replace("%temp%", "i")
tresc=tresc.replace("nigdy", "prawie nigdy")
tresc=tresc.replace("dlaczego", "czemu")
plik=open(nazwa,'w')
plik.write(tresc)
plik.close()