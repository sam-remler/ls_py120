import math


class Car():
    
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
    
    def __str__(self):
        return f"{self.color} {self.year} {self.model}"
    
    def __repr__(self):
        return f"Car({self.model}, {self.year}, {self.color})"



vwbuzz = Car('ID.Buzz', 2024, 'red')
print(vwbuzz)        # Red 2024 ID.Buzz
print(repr(vwbuzz))  # Car('ID.Buzz', 2024, 'red')

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)
    
    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vector(new_x, new_y)
    
    def __mul__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        dot_product = self.x * other.x + self.y * other.y
        return dot_product
    
    def __abs__(self):
        magnitude = math.sqrt((self.x ** 2 + self.y ** 2 ))
        return magnitude

    # __iadd__ method omitted; we don't need it for this exercise

    def __repr__(self):
        x = repr(self.x)
        y = repr(self.y)
        return f'Vector({x}, {y})'

v1 = Vector(5, 12)
v2 = Vector(13, -4)
print(v1 + v2)      # Vector(18, 8)

print(v1 - v2) # Vector(-8, 16)
print(v1 * v2) # 17
print(abs(v1)) # 13.0


# -----
print ( " ------- ")

class Candidate():
    def __init__(self, name):
        self.name = name
        self.votes = 0

    def __iadd__(self, number):
        if not isinstance(number, int):
            return NotImplemented
        
        self.votes += number

class Election():
    def __init__(self, candidates):
        self.candidates = candidates

    def results(self):
        for candidate in self.candidates:
            print(f"{candidate.name} : {candidate.votes} votes")
        
        winner = sorted(self.candidates, key = lambda x: x.votes, reverse=True)[0]
        total_votes = sum([candidate.votes for candidate in self.candidates])
        winning_percentage =  round((winner.votes / total_votes) * 100,1)

        print (f"{winner.name} won : {winning_percentage}% of votes")


mike_jones = Candidate('Mike Jones')
susan_dore = Candidate('Susan Dore')
kim_waters = Candidate('Kim Waters')

candidates = {
    mike_jones,
    susan_dore,
    kim_waters,
}

votes = [
    mike_jones,
    susan_dore,
    mike_jones,
    susan_dore,
    susan_dore,
    kim_waters,
    susan_dore,
    mike_jones,
]

for candidate in votes:
    candidate += 1

election = Election(candidates)
election.results()


class Vehicle:
    number_of_vehicles = 0

    def __init__(self):
        Vehicle.number_of_vehicles += 1

    @classmethod
    def vehicles(cls):
        return Vehicle.number_of_vehicles

class Car(Vehicle):

    def __init__(self):
        super().__init__()

class Truck(Vehicle):

    def __init__(self):
        super().__init__()

class Boat(Vehicle):

    def __init__(self):
        super().__init__()

# Test code omitted





print(Car.vehicles())     # 0
car1 = Car()
print(Car.vehicles())     # 1
car2 = Car()
car3 = Car()
car4 = Car()
print(Car.vehicles())     # 4
truck1 = Truck()
truck2 = Truck()
print(Truck.vehicles())   # 6
boat1 = Boat()
boat2 = Boat()
print(Boat.vehicles())    # 8    

class Cat:
    pass

whiskers = Cat()
ginger = Cat()
paws = Cat()

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.sound())

    def sound(self):
        return f'{self.name} says '

class Cow(Animal):
    def sound(self):
        return super().sound() + 'moooooooooooo!'

daisy = Cow('Daisy')
daisy.speak()



class Person:
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

kate = Person()
kate.name = 'Kate'
print(kate.name)

class Person:
    pass

kate = Person()
kate.name = 'Kate'
print(kate.name)

class Person:

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

mike = Person()
mike.first_name = 'Michael'
mike.last_name = 'Garcia'
print(mike.full_name)         # Michael Garcia

class Student:
    def __init__(self, name):
        self._name = name
        self._grade = None

    @property
    def grade(self):
        return self._grade
    
    def change_grade(self, grade):
        self._grade = grade

priya = Student('Priya')
priya.change_grade('A')
print(priya.grade)            # A