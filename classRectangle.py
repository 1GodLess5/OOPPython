# class Rectangle with function to get Area of it and trying how to use the class

class Rectangle:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

    def getArea(self):
        return self.width * self.height


blueRectangle = Rectangle(5, 4, "blue")

print(blueRectangle.getArea())
print(blueRectangle.color)
