class WalkMixin():
    def walk(self):
        print ( "Let's go for a walk!")


class Cat(WalkMixin):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def greet(self):
        print(f"Hello! My name is {self.name}!")

# Comments show expected output
kitty = Cat('Sophie')
kitty.greet()       # Hello! My name is Sophie!
kitty.walk()        # Let's go for a walk!


class TowingMixin:
    def tow(self):
        return 'I can tow a trailer!'

class Vehicle():
    def __init__(self, year):
        self.year = year

class Truck(Vehicle, TowingMixin):
    pass

class Car(Vehicle):
    pass

# Comments show expected output
truck1 = Truck(1994)
print(truck1.year)            # 1994
print(truck1.tow())           # I can tow a trailer!

car1 = Car(2006)
print(car1.year)              # 2006

