#!/usr/bin/env python
import random


def sortowanieMalejace(tab):
    for i in range(len(tab)):
        j=len(tab)-1
        while j>i:
            if tab[j]<tab[j-1]:
                tmp=tab[j]
                tab[j]= tab[j-1]
                tab[j-1]=tmp
            j-=1
    return tab

tab=[]


for i in range(50):
    tab.append(random.randint(-100,100))


print tab

tab=sortowanieMalejace(tab)

print tab

