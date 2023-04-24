class ValueTooSmallError(Exception):
    """Raised when the input value is too small"""
    pass

class ValueTooLargeError(Exception):
    """Raised when the input value is too large"""
    pass

# you need to guess this number
number = 10

# user guesses a number until he/she gets it right
while True:
    try:
        i_num = int(input("Ingrese un número: "))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("El valor es demasiado pequeño, pruebe de nuevo")
        print()
    except ValueTooLargeError:
        print("El valor es demasiado grande, pruebe de nuevo")
        print()

print("Congratulations! You guessed it correctly.")