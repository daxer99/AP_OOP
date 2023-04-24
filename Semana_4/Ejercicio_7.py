# class InvalidAgeError(Exception):
#     def __init__(self, msg):
#         self.__message = msg
#
#     def getMessage(self):
#         return self.__message

from InvalidAgeError import InvalidAgeError

def edad_voto(edad):
    if edad < 18:
        raise InvalidAgeError("El ciudadano no puede votar, su edad es " + str(edad))
    else:
        print('El ciudadano puede votar, su edad es', edad)

# calling function
try:
    edad_voto(22)
    edad_voto(14)
except InvalidAgeError as error:
    print(error)