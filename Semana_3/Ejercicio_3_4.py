from abc import ABC, abstractmethod
import math

class Figure(ABC):
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
      
    
class Rectangle(Figure):
    def __init__(self,base,altura):
        self.__base = base
        self.__altura = altura
        
    def base(self):
        return self.__base
    
    def altura(self):
        return self.__altura
    
    def area(self):
        return self.__base * self.__altura
    
    def perimeter(self):
        return self.__base + self.__altura
    
    def diagonal(self):
        return math.sqrt(pow(self.__base,2)+pow(self.__altura,2))
    
class Circle(Figure):
    def __init__(self,radio):
        self.__radio = radio
    
    def getRadio(self):
        return self.__radio
    
    def perimeter(self):
        return 2*math.pi*self.__radio
    
    def area(self):
        return math.pi*pow(self.__radio,2)

class Triangle(Figure):
    def __init__(self, sideA,sideB,sideC):
        self.__sideA = sideA
        self.__sideB = sideB
        self.__sideC = sideC
    
    def area(self):
        s = (self.__sideA + self.__sideB + self.__sideC) / 2
        area = math.sqrt(s*(s-self.__sideA)*(s-self.__sideB)*(s-self.__sideC)) #Heron's formula
        return area
    
    def perimeter(self):
        return self.__sideA + self.__sideB + self.__sideC

if __name__ == '__main__':
    r1 = Rectangle(2,3)
    r2 = Rectangle(5,8.9)
    c1 = Circle(3.2)
    c2 = Circle(4)
    t1 = Triangle(1,1,1)
    t2 = Triangle(2,2,1)

    figuras = [r1,r2,c1,c2,t1,t2]
    
    for figura in figuras:
        print('Area: ',figura.area())
        print('Perimeter: ', figura.perimeter())
        if isinstance(figura,Rectangle):
            print('Diagonal: ',figura.diagonal())




    
    
