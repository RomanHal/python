#!/usr/bin/env python

import numpy

X = numpy.random.random((10, 10))

det = numpy.linalg.det(X)

print det
