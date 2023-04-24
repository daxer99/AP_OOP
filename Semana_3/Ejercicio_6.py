class Point2D:
    
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
        
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def __str__(self):
        return 'X = ' + str(self.__x) + ',' + 'Y = ' + str(self.__y)

class Point3D_1(Point2D):
    def __init__(self,x,y,z):
        Point2D.__init__(self,x,y)
        self.__z = z
    
    def getZ(self):
        return self.__z
    
    def __str__(self):
        return Point2D.__str__(self) + ',' + 'Z = '+ str(self.__z)

class Point3D_2:
    def __init__(self,x,y,z):
        self.__x = x
        self.__y = y
        self.__z = z
    
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def getZ(self):
        return self.__z
    
    def __str__(self):
        return 'X = ' + str(self.__x) + ',' + 'Y = ' + str(self.__y) +',' +'Z = '+ str(self.__z)
    
if __name__ == '__main__':
    p1 = Point3D_1(1,2,3)
    print(p1)
    p2 = Point3D_2(1,2,3)
    print(p2)
    