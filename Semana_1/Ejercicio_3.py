import math as m

class Point2D:
    maxDistanceToOrigin = 0

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getDistance(self,point):
        return m.sqrt(pow(self.__x - point.getX(), 2) + pow(self.__y - point.getY(), 2))

    def add(self,point):
        return Point2D(self.__x + point.getX(),self.__y + point.getY())

    @classmethod
    def getDistanceToOrigin(cls, point):
        distancia = m.sqrt(pow(0 - point.getX(), 2) + pow(0 - point.getY(), 2))
        if distancia > Point2D.maxDistanceToOrigin:
            Point2D.maxDistanceToOrigin = distancia
        return distancia

    def __str__(self):
        return '(X = ' + str(self.__x) + ',' + 'Y = ' + str(self.__y) + ')'


if __name__ == '__main__':
    p1 = Point2D(1, 1)
    p2 = Point2D(2, 2)
    p3 = p1.add(p2)

    print(p3)

    print(Point2D.maxDistanceToOrigin)
    Point2D.getDistanceToOrigin(p1)
    print(Point2D.maxDistanceToOrigin)
    Point2D.getDistanceToOrigin(p2)
    print(Point2D.maxDistanceToOrigin)