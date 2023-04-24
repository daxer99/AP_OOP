import math
import sys

def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact


number_list = [10, -5, 1.2, 'apple']

for number in number_list:
    try:
        number_factorial = factorial(number)
    except TypeError:
        print("Factorial no soporta ese tipo de dato.")
    except ValueError:
        print("Factorial solo acepta enteros positivos.", number, " no es entero positivo.")
    else:
        print("El factorial de ", number, "es", number_factorial)



# try:
#     result = math.factorial(2.4)
# except:
#     print("Something Unexpected has happened.", sys.exc_info()[0])
# else:
#     print("The factorial is", result)