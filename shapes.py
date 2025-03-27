# shapes.py
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

if __name__ == "__main__":
    circle = Circle(5)
    square = Square(4)
    print("Circle area:", circle.area())
    print("Square area:", square.area())

def perimeter(self):
    return 2 * 3.14 * self.radius
