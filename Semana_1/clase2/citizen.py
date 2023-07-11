class Citizen:
    def __init__(self, dni, first_name, last_name, age):
        self.__dni = dni
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age

    def getDNI(self):
        return self.__dni
    def getFirstName(self):
        return self.__first_name
    def getLastName(self):
        return self.__last_name
    def getAge(self):
        return self.__age

    def __eq__(self, other):
        return (self.__dni, self.__first_name, self.__last_name) == (
        other.getDNI(), other.getFirstName(), other.getLastName())

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return self.__age < other.getAge()

    def __gt__(self, other):
        return self.__age > other.getAge()

    def __le__(self, other):
        return self.__age <= other.getAge()

    def __ge__(self, other):
        return self.__age >= other.getAge()
    @classmethod
    def mayor_que(cls,c1,c2):
        return c1.getAge() > c2.getAge()

if __name__ == '__main__':
    ciudadano1 = Citizen(1, 'rodrigo', 'peralta', 29)
    ciudadano0 = Citizen(1, 'rodrigo', 'peralta', 29)
    print(id(ciudadano0))
    print(id(ciudadano1))
    ciudadano2 = Citizen(7, 'luciana', 'paez', 28)

    # print(ciudadano1 == ciudadano0)
    # print(ciudadano1 == ciudadano2)
    # print(ciudadano1 > ciudadano2)
    print(Citizen.mayor_que(ciudadano1,ciudadano2))

