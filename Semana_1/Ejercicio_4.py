import math
from Ejercicio_3 import Point2D

class Circle:
    def __init__(self, center, radio):
        self.__center = center
        self.__radio = radio

    def center(self):
        return self.__center

    def perimeter(self):
        return 2 * math.pi * self.__radio

    def area(self):
        return math.pi * pow(self.__radio, 2)

    def contains(self, point2d):
        return pow((self.__center.getX() - point2d.getX()), 2) - pow((self.__center.getY() - point2d.getY()), 2) <= pow(
            self.__radio, 2)


if __name__ == '__main__':
    center = Point2D(1, 1)
    circle = Circle(center, 3)
    print(circle.center())
    print('El perimetro es: ', circle.perimeter())
    print('El area es: ', circle.area())

    point = Point2D(0, 1)

    if circle.contains(point):
        print(point, 'se encuentra en el circulo')
    else:
        print(point, ' no se encuentra en el circulo')
