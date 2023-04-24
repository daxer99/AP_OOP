class InvalidAgeError(Exception):
    def __init__(self, msg):
        self.__message = msg

    def getMessage(self):
        return self.__message