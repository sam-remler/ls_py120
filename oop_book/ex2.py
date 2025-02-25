class Person():
    def __init__(self, first_name : str, last_name : str):
        self._first_name = first_name
        self._last_name = last_name
    
    @property
    def first_name(self):
        return self._first_name
    
    @property
    def last_name(self):
        return self._last_name
    
    @property
    def name(self):
        return (self._first_name, self._last_name)
    
    @first_name.setter
    def first_name(self, first_name : str):
        if not first_name.isalpha():
            raise ValueError
        self._first_name = first_name

    @last_name.setter
    def last_name(self, last_name : str):
        if not last_name.isalpha():
            raise ValueError
        self._last_name = last_name
    
    @name.setter
    def name(self, name : tuple):
        if not (name[0].isalpha() or name[1].isalpha()):
            raise ValueError
        (self._first_name, self._last_name) = name
    
    def get_name(self):
        print (f"Your name is {self.first_name.capitalize()} {self.last_name.capitalize()}")

actor = Person('Mark', 'Sinclair')
print(actor.name)              # Mark Sinclair
actor.name = ('Vin', 'Diesel')
print(actor.name)              # Vin Diesel
actor.name = ('', 'Diesel')
# ValueError: Name must be alphabetic.