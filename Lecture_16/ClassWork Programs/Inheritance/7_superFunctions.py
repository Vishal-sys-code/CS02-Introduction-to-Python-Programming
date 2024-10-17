class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

class Square(Rectangle):
    def __init__(self,length,width):
        super().__init__(length,width)
    def area(self):
        return self.length * self.width

class Cube(Rectangle):
    def __init__(self,length, width, height):
        super().__init__(length, width)
        self.height = height
    def volume(self):
        return self.length * self.width * self.width

square_obj = Square(3,3)
cube_obj = Cube(3,3,3)
a = square_obj.area()
b = cube_obj.volume()
print(a)
print(b)

"""
Output:
9 
27
"""