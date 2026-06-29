# -- finding the area of a circle
import math

def areaOfCircle(radius):
    pi = math.pi
    if radius <= 0:
        raise ValueError('Radius cannot be zero or negative')
    return round(pi*(radius**2), 2)

print(areaOfCircle(0))

