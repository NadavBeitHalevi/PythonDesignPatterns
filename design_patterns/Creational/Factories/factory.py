# The Factory Method Pattern
# A component responsible solely for the wholesale (not piecewise) creation of objects.
# when to use: when a class can't anticipate the class of objects it must create.
#  Using a static methid to create an object.
from abc import ABC, abstractmethod
from enum import Enum
import math

class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)
    
    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * math.cos(theta), rho * math.sin(theta))

# Factory class <-- move the factory methods to a separate class (below)
class PointFactory:
    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)
    
    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * math.cos(theta), rho * math.sin(theta))

if __name__ == '__main__':
    p = Point.new_cartesian_point(1, 2)
    print(p.x, p.y)
    p = Point.new_polar_point(1, 2)
    print(p.x, p.y)