from abc import ABC

class HotDrink(ABC):
    def consume(self):
        pass

class Tea(HotDrink):
    def consume(self):
        print('This tea is delicious.')

class Coffee(HotDrink):
    def consume(self):
        print('This coffee is delicious.')

class HotDrinkFactory(ABC):
    def prepare(self, amount):
        pass

        class TeaFactory(HotDrinkFactory):
            def prepare(self, amount):
                print(f'Put in tea bag, boil water, pour {amount}ml, add lemon')
                return Tea()

        class CoffeeFactory(HotDrinkFactory):
            def prepare(self, amount):
                print(f'Grind some beans, boil water, pour {amount}ml, add cream and sugar')
                return Coffee()

        def make_drink(type):
            if type == 'tea':
                return TeaFactory().prepare(200)
            elif type == 'coffee':
                return CoffeeFactory().prepare(50)
            else:
                return None
# ===
from unittest import TestCase


class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class PersonFactory:
    id = 0

    def create_person(self, name):
        p = Person(PersonFactory.id, name)
        PersonFactory.id += 1
        return p

class Evaluate(TestCase):
    def test_exercise(self):
        pf = PersonFactory()

        p1 = pf.create_person('Chris')
        self.assertEqual(p1.name, 'Chris')
        self.assertEqual(p1.id, 0)

        p2 = pf.create_person('Sarah')
        self.assertEqual(p2.id, 1)
