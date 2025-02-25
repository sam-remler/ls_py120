class Rectangle():
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height
    
    @width.setter
    def width(self, width):
        if isinstance(width, int):
            self._width = width
    
    @height.setter
    def height(self, height):
        if isinstance(height, int):
            self._height = height
    
    @property
    def area(self):
        return self._height * self._width


rect = Rectangle(4, 5)

print(rect.width == 4)
print(rect.height == 5)       
print(rect.area == 20)        

rect.width = 6
print(rect.area == 30)


rect.height = 6
print(rect.area == 36)



class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

square = Square(5)
print(square.area == 25)      # True