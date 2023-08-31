class PasswordTooShortError(Exception):
    def __init__(self, length, message="Password is too short"):
        self.length = length
        self.message = message

def validate_password(password):
    if len(password) < 8:
        raise PasswordTooShortError(len(password))
try:
    validate_password("abc1111")
except PasswordTooShortError as error:
    print(error.message, "Length:", error.length)