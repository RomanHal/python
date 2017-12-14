#!/usr/bin/env python

plik=open("plik.txt",'w')

plik.write("jakies wazne dane itd.")

plik.close()

plik=open("plik.txt")
print plik.read()
