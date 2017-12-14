#!/usr/bin/env python
import os

print (sum(os.path.isdir(i) for i in os.listdir(".")))

