#!/usr/bin/env python

import math

class Zespolona:
    def __init__(self, rzeczywista, urojona):
        self.r = rzeczywista
        self.i = urojona

    def __add__(self, other):
        return Zespolona(self.r+other.r, self.i+other.i)

    def __sub__(self, other):
        return Zespolona(self.r-other.r,self.i-other.i)

    def modul(self):
        return math.sqrt(self.r * self.r + self.i * self.i)


x=Zespolona(1,2)
y=Zespolona(3,4)

z = x+y

print x.modul()
