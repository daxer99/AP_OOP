class Book:
    def __init__(self, title, author, id):
        self.title = title
        self.author = author
        self.id = id

class User:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

class Transaction:
    def __init__(self, book_id, user_id, issue_date, return_date):
        self.book_id = book_id
        self.user_id = user_id
        self.issue_date = issue_date
        self.return_date = return_date

class Library:
    books = []
    users = []
    transactions = []

    def add_book(self, title, author, id):
        self.books.append(Book(title, author, id))

    def remove_book(self, id):
        for book in self.books:
            if book.id == id:
                self.books.remove(book)

    def add_user(self, name, email, phone):
        self.users.append(User(name, email, phone))

    def remove_user(self, email):
        for user in self.users:
            if user.email == email:
                self.users.remove(user)

    def issue_book(self, book_id, user_id, issue_date, return_date):
        self.transactions.append(Transaction(book_id, user_id, issue_date, return_date))

    def return_book(self, book_id, user_id, return_date):
        for transaction in self.transactions:
            if transaction.book_id == book_id and transaction.user_id == user_id:
                transaction.return_date = return_date
                break