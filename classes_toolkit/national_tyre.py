"""sub-class implementation, inheriting from 'Circle' within circuituous mod"""

from circuituous import Circle


class Tire(Circle):
    "Tires are circles with a corrected perimeter"


    def perimeter(self):
        "Circumference corrected for the rubber"
        ODO_CORRECT = 1.25      # method variable
        return Circle.perimeter(self) * ODO_CORRECT 


t = Tire(22)

print()
print('A tire of radius', t.radius)
print('has an inner area of', t.area())
print('and an odometer corrected perimeter of')
print(t.perimeter())
print()

