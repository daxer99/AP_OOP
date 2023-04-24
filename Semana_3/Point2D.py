import math as m
class Point2D:
    
    distanciaMaximaAlOrigen = 0
    
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
    
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def getDistance(self,punto):
        return m.sqrt(pow(self.__x-punto.getX(),2)+ pow(self.__y-punto.getY(),2))

    def __str__(self):
        return '(X = ' + str(self.__x) + ',' + 'Y = ' + str(self.__y) +')'