"""Alternate constructor required to provide custom api"""

from circuituous import Circle


BBD = 25

c = Circle.from_bbd(BBD)

print()
print('A circle with a bbd of', BBD)
print('has a radius of', c.radius)
print('and an area of', c.area())
print()

