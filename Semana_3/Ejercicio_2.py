import math
from Point2D import Point2D

class Circle:
    def __init__(self,center, radio):
        self.__center = center
        self.__radio = radio
    
    def getRadio(self):
        return self.__radio
    
    def center(self):
        return self.__center
    
    def perimeter(self):
        return 2*math.pi*self.__radio
    
    def area(self):
        return math.pi*pow(self.__radio,2)
    
    def contains(self, point2d):
        return pow((self.__center.getX()-point2d.getX()),2) - pow((self.__center.getY()-point2d.getY()),2) <= pow(self.__radio,2)

class Cylinder:
    def __init__(self,circle,hight):
        self.__circle = circle
        self.__hight = hight
        
    def area(self):
        return self.__circle.perimeter()*(self.__circle.getRadio() + self.__hight)
    
    def volumen(self):
        return self.__circle.area()*self.__hight
    
if __name__ == '__main__':
    p1 = Point2D(1,1)
    c1 = Circle(p1,2)
    cy1 = Cylinder(c1,5)
    print(c1.area())
    print(cy1.volumen())