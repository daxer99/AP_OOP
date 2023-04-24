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

class Cylinder(Circle):
    def __init__(self,center,radio,hight):
        Circle.__init__(self,center,radio)
        self.__hight = hight
        
    def area(self):
        return Circle.perimeter(self)*(Circle.getRadio(self) + self.__hight)
    
    def volumen(self):
        return Circle.area(self)*self.__hight
    
if __name__ == '__main__':
    p1 = Point2D(1,1)
    cy1 = Cylinder(p1,2,5)
    print(cy1.area())
    print(cy1.volumen())