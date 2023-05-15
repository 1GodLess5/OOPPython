from abc import ABC, abstractmethod
import math
import os
class Shape(ABC):
    def __init__(self, sidesLengths):
        self.sidesLengths = sidesLengths

    @abstractmethod
    def getArea(self):
        pass

    @abstractmethod
    def getSurface(self):
        pass


class Triangle(Shape):
    def __init__(self, sidesLengths):
        super().__init__(sidesLengths)

    def getArea(self):
        a = self.sidesLengths[0]
        b = self.sidesLengths[1]
        c = self.sidesLengths[2]

        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))

        return area

    def getSurface(self):
        return self.sidesLengths[0] + self.sidesLengths[1] + self.sidesLengths[2]


class Square(Shape):
    def __init__(self, sidesLengths):
        super().__init__(sidesLengths)

    def getArea(self):
        return self.sidesLengths[0] * self.sidesLengths[0]

    def getSurface(self):
        return 4 * self.sidesLengths[0]


class Rectangle(Shape):
    def __init__(self, sidesLengths):
        super().__init__(sidesLengths)

    def getArea(self):
        return self.sidesLengths[0] * self.sidesLengths[1]

    def getSurface(self):
        return 2 * (self.sidesLengths[0] + self.sidesLengths[1])

class Circle(Shape):
    def __init__(self, sidesLengths):
        super().__init__(sidesLengths)

    def getArea(self):
        return math.pi * (self.sidesLengths[0] * self.sidesLengths[0])

    def getSurface(self):
        return 2 * math.pi * self.sidesLengths[0]


shape = 1
sides = []

while shape != 0:
    letter = ord("a")

    print("1\t-\tTriangle")
    print("2\t-\tSquare")
    print("3\t-\tRectangle")
    print("4\t-\tCircle")
    print("0\t-\tExit()")

    shape = int(input("Choose shape: "))
    

    match shape:
        case 0:
            continue

        case 1:
            for i in range(3):
                # ord() takes letter, chr() takes number
                sides.append(float(input("Enter length of side '" + chr(letter) + "' in cm: ")))
                letter += 1

            triangle = Triangle(sides)
            print("Area of your triangle is: {:.2f}".format(triangle.getArea()) + " cm2")
            print("Surface of you triangle is: {:.2f}".format(triangle.getSurface()) + " cm")

        case 2:
            sides.append(float(input("Enter length of side 'a': ")))

            square = Square(sides)
            print("Area of your square is: {:.2f}".format(square.getArea()) + " cm2")
            print("Surface of your square is: {:.2f}".format(square.getSurface()) + " cm")

        case 3:
            for i in range(2):
                sides.append(float(input("Enter length of side '" + chr(letter) + "' in cm: ")))
                letter += 1

            rectangle = Rectangle(sides)
            print("Area of your rectangle is: {:.2f}".format(rectangle.getArea()) + "cm2")
            print("Surface of your rectangle is: {:.2f}".format(rectangle.getSurface()) + "cm")

        case 4:
            sides.append(float(input("Enter radius of your circle in cm: ")))

            circle = Circle(sides)
            print("Area of your circle is: {:.2f}".format(circle.getArea()) + "cm2")
            print("Surface of your circle is: {:.2f}".format(circle.getSurface()) + "cm")

        case _:
            print("Enter existing value!")

    sides.clear()
    