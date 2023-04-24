class Rectangle:
    def __init__(self,b,h):
        self.__base = b
        self.__height = h

    def calculateArea(self):
        return self.__base*self.__height

if __name__ == '__main__':

    r1 = Rectangle(10,5)
    print('Area: ',str(r1.calculateArea()))