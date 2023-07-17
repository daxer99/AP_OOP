class Book:
    def __init__(self,id,title,author,publish_year):
        self.__id=id
        self.__title = title
        self.__author = author
        self.__publish_year = publish_year
    def get_id(self):
        return self.__id
    def get_title(self):
        return self.__title
    def get_author(self):
        return self.__author
    def get_publish_year(self):
        return self.__publish_year
    def __str__(self):
        return "Id: "+str(self.__id) + ". Title: "+self.__title + ". Author: "+self.__author + ". Publish year: "+str(self.__publish_year)

class Library:
    def __init__(self,ID,nombre):
        self.__ID = ID
        self.__nombre = nombre
        self.__books = []
#Agregacion
    # def add_book(self,book):
    #     self.__books.append(book)

#Composicion
    def add_book(self,id,title,author,publish_year):
        book = Book(id,title,author,publish_year)
        self.__books.append(book)

    def order_by_title(self):
        return sorted(self.__books,key = lambda x:x.get_title())
    def order_by_year(self):
        return sorted(self.__books,key = lambda x:x.get_publish_year())

if __name__ == '__main__':
#Agregacion
    # libro1 = Book(1,"Martin Fierro", "Hernandez, Jose",1872)
    # libro2 = Book(2, "1984", "Orwell, George", 1949)
    # libro3 = Book(3, "Moby Dick", "Melville, Herman", 1851)
    # libro4 = Book(4, "Frankenstein", "Shelly, Mary", 1818)
    #
    # biblioteca = Library(1,"l1")
    # biblioteca.add_book(libro1)
    # biblioteca.add_book(libro2)
    # biblioteca.add_book(libro3)
    # biblioteca.add_book(libro4)
#Composicion
    biblioteca = Library(1,"l1")
    biblioteca.add_book(1,"Martin Fierro", "Hernandez, Jose",1872)
    biblioteca.add_book(2, "1984", "Orwell, George", 1949)
    biblioteca.add_book(3, "Moby Dick", "Melville, Herman", 1851)
    biblioteca.add_book(4, "Frankenstein", "Shelly, Mary", 1818)

    print("Libros disponibles, ordenados por año")
    sorted_year = biblioteca.order_by_year()
    for i in sorted_year:
        print(i)
    print("Libros disponibles, ordenados por titulo")
    sorted_title = biblioteca.order_by_title()
    for i in sorted_title:
        print(i)