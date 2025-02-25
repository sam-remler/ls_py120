class Car():
    def __init__(self, model, year, color):
        self._model = model
        self._year = year
        self._color = color
        self._current_speed = 0

    def engine_start(self):
        print ("The engine is on!")

    def speed_up(self, number):
        self._current_speed += number
        print ("We are accelerating!")

    def brake(self, number):
        self._current_speed -= number
        print ("We are braking!")

    def engine_off(self):
        self._current_speed = 0
        print ("The engine is off!")

    def get_speed(self):
        print( f"The car's current speed is {self._current_speed}" )

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def model(self):
        return self._model

    @property
    def year(self):
        return self._year
    
    def spray_paint(self, color):
        self.color = color



lumina = Car('chevy lumina', 1997, 'white')
lumina.engine_start() # The engine is on!
lumina.get_speed()    # Your speed is 0 mph.
lumina.speed_up(20)   # You accelerated 20 mph.
lumina.get_speed()    # Your speed is 20 mph.
lumina.speed_up(30)   # You accelerated 30 mph.
lumina.get_speed()    # Your speed is 50 mph.
lumina.brake(15)      # You decelerated 15 mph.
lumina.get_speed()    # Your speed is 35 mph.
lumina.brake(30)      # You decelerated 30 mph.
lumina.get_speed()    # Your speed is 5 mph.
lumina.engine_off()   # Let's park this baby!
                      # The engine is off
lumina.get_speed()    # Your speed is 0 mph.


print(f'My car is {lumina.color}.')
# My car is white.

print(f"My car's model is a {lumina.model}.")
# My car's model is a chevy lumina.

print(f"My car's year is {lumina.year}.")
# My car's year is 1997.

lumina.color = 'brown'
print(f'My car is now {lumina.color}.')
# My car is now brown.