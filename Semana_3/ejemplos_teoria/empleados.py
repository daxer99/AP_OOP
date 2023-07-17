from abc import abstractmethod

class Employee:
    def __init__(self,dni,first_name,last_name):
        self.__dni = dni
        self.__first_name = first_name
        self.__last_name = last_name
        self.__projects = []

    def get_dni(self):
        return self.__dni
    def get_first_name(self):
        return self.__first_name
    def get_last_name(self):
        return self.__last_name
    @abstractmethod
    def calculate_salary(self):
        pass
    def assign_project(self,project):
        self.__projects.append(project)
    def get_projects(self):
        return self.__projects

class Junior(Employee):
    def __int__(self,dni,first_name,last_name,regular_salary):
        Employee.__init__(self,dni,first_name,last_name)
        self.__regular_salary = regular_salary

    def update_regular_salary(self,amount):
        self.__regular_salary = amount

    def calculate_salary(self):


