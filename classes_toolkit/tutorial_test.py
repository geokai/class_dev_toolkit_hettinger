'''Tutorial test script'''

from circuituous import Circle


# Tutorial

print()
print('circuituous version', Circle.version)

c = Circle(10)

print('A circle of radius', c.radius)
print('has an area of', c.area())
print()
