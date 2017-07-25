"""Implementing Circuituous (tm) 'area' method on a range of circles."""

from circuituous import Circle
from random import random, seed


print()
print('Using Circuituous (tm) version', Circle.version)
print()

seed(8675309)
n = 10
circles = [Circle(random()) for i in range(n)]

print('The average area of', n, 'random circles ', end='')
avg = sum([c.area() for c in circles]) / n
print('is {0:0.3f}'.format(avg))

print()
