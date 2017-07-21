"""Circuituous, LLC -- An Advanced Circle Analytics Company"""
# Include a Module DocString for your module:

import math

# Document your class and methods:
class Circle(object):                       # new style class
    "An advanced circle analytic toolkit"

    version = '0.2'                         # class variable

    def __init__(self, radius):
        self.radius = radius                # instance variable


    def area(self):
        "Perform quarrature on a shape of uniform radius"
        return math.pi * self.radius ** 2.0


    def perimeter(self):
        return 2.0 * math.pi * self.radius

