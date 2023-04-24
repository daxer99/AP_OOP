import math

class Point2D:
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
    
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def getDistance(self,point):
        return math.sqrt(pow(self.__x - point.getX(),2) + pow(self.__y - point.getY(),2))
    

class Line:
    def __init__(self,p1,p2):
        self.__a = p1
        self.__b = p2
        
    def getA(self):
        return self.__a
    
    def getB(self):
        return self.__b
    
    def getLength(self):
        return self.__a.getDistance(self.__b)
    
class Triangle:
    def __init__(self,x,y,z):
        self.__sideA = x
        self.__sideB = y
        self.__sideC = z

    def area(self):
        s = (self.__sideA.getLength() + self.__sideB.getLength() + self.__sideC.getLength()) / 2
        area = math.sqrt(s*(s-self.__sideA.getLength())*(s-self.__sideB.getLength())*(s-self.__sideC.getLength())) #Heron's formula
        return area
    
    def perimeter(self):
        return self.__sideA.getLength() + self.__sideB.getLength() + self.__sideC.getLength()
    
    def is_valid(self):
        return (self.__sideA.getLength()+self.__sideB.getLength()>=self.__sideC.getLength() 
            and self.__sideB.getLength()+self.__sideC.getLength()>=self.__sideA.getLength() 
            and self.__sideC.getLength()+self.__sideA.getLength()>=self.__sideB.getLength())
    
    def is_scalene(self):
        return ((self.__sideA.getLength() != self.__sideB.getLength()) 
                and (self.__sideA.getLength() != self.__sideC.getLength()) 
                and (self.__sideB.getLength() != self.__sideC.getLength()))
    
    def is_equilateral(self):
        return (self.__sideA.getLength() == self.__sideB.getLength()) and (self.__sideA.getLength() == self.__sideC.getLength())
    
    def is_isoceles(self):
        return (((self.__sideA.getLength() == self.__sideB.getLength())and(self.__sideA.getLength() != self.__sideC.getLength()))
                or((self.__sideA.getLength() == self.__sideC.getLength())and(self.__sideA.getLength() != self.__sideB.getLength()))
                or((self.__sideB.getLength() == self.__sideC.getLength())and(self.__sideB.getLength() != self.__sideA.getLength())))
    
    def __str__(self):
        return '(Triangle: ' + str(self.__sideA.getLength()) +','+ str(self.__sideB.getLength()) +','+ str(self.__sideC.getLength()) +')'

if __name__ == '__main__':
  
    l3 = Line(Point2D(0,0),Point2D(0,3))  
    l4 = Line(Point2D(0,0),Point2D(0,4))
    l6 = Line(Point2D(0,0),Point2D(0,6))  
    l8 = Line(Point2D(0,0),Point2D(0,8)) 
    l12 = Line(Point2D(0,0),Point2D(0,12))  
    l20 = Line(Point2D(0,0),Point2D(0,20))  
    
    t1 = Triangle(l4,l8,l6)
    t2 = Triangle(l6,l6,l12)
    t3 = Triangle(l3,l3,l3)
    t4 = Triangle(l3,l6,l20)
        
    # t1 = Triangle(4,8,6)
    # t2 = Triangle(6,6,12)
    # t3 = Triangle(3,3,3)
    # t4 = Triangle(3,6,20)

    
    lista_triangles = [t1,t2,t3,t4]
    
    for triangle in lista_triangles:
        if triangle.is_valid():
            if triangle.is_equilateral():
                print(triangle,'es equilatero')
            elif triangle.is_isoceles():
                print(triangle,'es isoceles')
            elif triangle.is_scalene():
                print(triangle,'es escaleno')
        else:
            print(triangle,'no es un triangulo valido')        