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
    def __init__(self,id,first_name,last_name,regular_salary):
        Employee.__init__(self,id,first_name,last_name)
        self.__regular_salary = regular_salary

    def update_regular_salary(self,amount):
        self.__regular_salary = amount

    def calculate_salary(self):
        salary = self.__regular_salary + self.__regular_salary * 0.03 * len(self.get_projects())
        return salary

class Senior(Employee):
    def __init__(self, id, first_name, last_name,regular_salary):
        Employee.__init__(self, id, first_name, last_name)
        self.__regular_salary = regular_salary
        self.__in_charge = []

    def assign_junior(self,junior):
        if len(self.__in_charge) <= 3:
            self.__in_charge.append(junior)
    def get_in_charge(self):
        return self.__in_charge
    def update_regular_salary(self,amount):
        self.__regular_salary = amount
    def calculate_salary(self):
        salary = self.__regular_salary + self.__regular_salary * 0.11 * len(self.get_in_charge())
        return salary
    def get_regular_salary(self):
        return self.__regular_salary

class Leader(Senior):
    def __int__(self,dni,first_name,last_name,regular_salary):
        Senior.__init__(self,dni,first_name,last_name,regular_salary)

    def calculate_salary(self):
        salary = Senior.get_regular_salary(self) + Senior.get_regular_salary(self) * 0.11 * len(self.get_in_charge()) + Senior.get_regular_salary(self) * 0.15
        return salary

class Project:
    pass

junior_salary = 750
senior_salary = 1500
junior_1 = Junior(1,"Juan","Perez",junior_salary)
junior_2 = Junior(2,"Lucia","Shaw",junior_salary)
junior_3 = Junior(3,"Mariano","Lopez",junior_salary)
senior_1 = Senior(4,"Fernando","Juarez",senior_salary)
senior_2 = Senior(4,"William","Wallace",senior_salary)
leader = Leader(4,"Santiago","Garcia",senior_salary)

p1 = Project()
p2 = Project()
p3 = Project()
p4 = Project()
p5 = Project()

junior_1.assign_project(p1)
junior_2.assign_project(p1)
junior_2.assign_project(p2)
senior_1.assign_project(p1)
senior_1.assign_junior(junior_1)
senior_1.assign_junior(junior_2)
leader.assign_project(p1)


print("Salary junior_1: ",junior_1.calculate_salary())
print("Salary junior_2: ",junior_2.calculate_salary())
print("Salary senior_1: ",senior_1.calculate_salary())
print("Salary leader: ",leader.calculate_salary())