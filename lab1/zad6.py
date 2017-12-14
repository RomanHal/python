#!/usr/bin/env python

import Image
print ("nazwa pliku .jpg bez rozszerzenia do konversji na .png")
nazwa=raw_input()
im =Image.open(nazwa+".jpg")
im.save(nazwa+".png")
