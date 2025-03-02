# write using test for factory pattern
# test if the factory pattern is working as expected

import unittest

class Car:
    def __init__(self, name):
        self.name = name

class Toyota(Car):
    def __init__(self):
        super().__init__("Toyota")

class CarFactory: 
    def get_car(self, name):
        if name == "Toyota":
            return Toyota()
        else:
            return None


class TestFactory_test(unittest.TestCase):
    def test_toyota_factory(self):
        print("Testing Toyota Factory")
        car_factory = CarFactory()
        car = car_factory.get_car("Toyota")
        self.assertEqual(car.name, "Toyota")
    
    def test_invalid_car(self):
        print("Testing Invalid Car")
        car_factory = CarFactory()
        car = car_factory.get_car("Invalid")
        self.assertIsNone(car)