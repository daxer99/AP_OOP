class Student:
    def __init__(self,dni,first_name,last_name,age):
        self.__dni = dni
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age

    def get_dni(self):
        return self.__dni
    def get_first_name(self):
        return self.__first_name
    def get_last_name(self):
        return self.__last_name
    def get_age(self):
        return self.__age
    def make_homework(self):
        pass
    def take_exam(self):
        pass
    def __str__(self):
        return self.__first_name +" "+self.__last_name

class Teacher:
    def __init__(self,dni,first_name,last_name,position):
        self.__dni = dni
        self.__first_name = first_name
        self.__last_name = last_name
        self.__position = position

    def get_dni(self):
        return self.__dni
    def get_first_name(self):
        return self.__first_name
    def get_last_name(self):
        return self.__last_name
    def get_position(self):
        return self.__position
    def correct_homework(self):
        pass
    def correct_exam(self):
        pass
    def take_attendance(self):
        pass

class Course:
    def __init__(self,id,name,teacher):
        self.__id = id
        self.__name = name
        self.__teacher = teacher
        self.__students = []

    def enroll_student(self,dni,first_name,last_name,age):
        student = Student(dni,first_name,last_name,age)
        self.__students.append(student)

    def list_students(self):
        students_list = []
        for i in self.__students:
            students_list.append(i.__str__())
        return students_list

if __name__ == '__main__':
    maestro = Teacher(1,"Ana","Perez","Titular")
    maestro2 = Teacher(2,"Juan","Ruhl","Titular")
    biologia = Course("bio1","Biologia",maestro)
    historia = Course("his1","Historia",maestro2)

    biologia.enroll_student(12,"Luis","Lopez",15)
    biologia.enroll_student(15, "Maria", "Paez", 14)
    biologia.enroll_student(177, "Sofia", "Reyes", 15)

    historia.enroll_student(12,"Luis","Lopez",15)
    historia.enroll_student(15, "Lucas", "Aguirre", 15)
    historia.enroll_student(177, "Sofia", "Reyes", 15)

    listado_biologia = biologia.list_students()
    listado_historia = historia.list_students()

    print("Listado de alumnos inscriptos en Biologia:")
    for i in listado_biologia:
        print(i)

    print("\nListado de alumnos inscriptos en Historia:")
    for i in listado_historia:
        print(i)
