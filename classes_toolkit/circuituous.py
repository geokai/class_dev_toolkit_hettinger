"""Circuituous, LLC -- An Advanced Circle Analytics Company."""

import math


class Circle(object):                       # new style class
    """An advanced circle analytic toolkit."""

    version = '0.3'                         # class variable

    def __init__(self, radius):
        self.radius = radius                # instance variable


    def area(self):
        """Perform quarrature on a shape of uniform radius."""
        return math.pi * self.radius ** 2.0


    def perimeter(self):
        """Evaluate the perimeter length of the circle object."""
        return 2.0 * math.pi * self.radius

    @classmethod                            # alternative constructor
    def from_bbd(cls, bbd):
        """Construct a circle from a bounding box diagonal."""
        radius = bbd / 2.0 / math.sqrt(2.0)
        return cls(radius)

