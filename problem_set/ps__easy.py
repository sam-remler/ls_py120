class Greeting:
    def greet(self, message):
        print(message)

class Hello(Greeting):
    def hi(self):
        self.greet('Hello')

class Goodbye(Greeting):
    def bye(self):
        self.greet('Goodbye')

hello = Hello()
#hello.hi() #Hello

hello = Hello()
#hello.bye() # Error

hello = Hello()
#hello.greet() # Error

hello = Hello()
#hello.greet('Goodbye') # GoodBye

#Hello.hi() # Error


class Television:
    @classmethod
    def manufacturer(cls):
        return 'Amazon'

    def model(self):
        return 'Omni Fire'

tv = Television()
print(tv.manufacturer()) # Amazon
print(tv.model()) # OmniFire

print(Television.manufacturer()) # Amazon
print(Television.model()) # Error