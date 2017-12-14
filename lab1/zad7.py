#!/usr/bin/env python
import math

print ("ax^2+bx+c=0 podaj a,b,c; a ma byc wieksze od 0")
a,b,c=raw_input().split()
a=int(a)
b=int(b)
c=int(c)

delta=b*b-4*a*c

if(delta<0):
    print ("brak rozw")
elif(delta==0):
    x0=-b/2*a
    print "x=",x0
elif(delta>0):
    x1=((-b-math.sqrt(delta))/2*a)
    x2=((-b+math.sqrt(delta))/2*a)
    print "x1 =",x1
    print "x2 =" ,x2
