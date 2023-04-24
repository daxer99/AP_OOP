class Citizen:
    def __init__(self, dni,first_name, last_name, age):
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
        return (self.__dni,self.__first_name, self.__last_name) == (other.getDNI(),other.getFirstName(), other.getLastName())

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
    
if __name__ == '__main__':
    c1 = Citizen(1,'r','p',27)
    c0 = Citizen(1,'r','p',27)
    c2 = Citizen(7,'l','p',28)
    
    print(c1==c0)
    print(c1 == c2)

    