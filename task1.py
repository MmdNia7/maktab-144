from abc import ABC,abstractmethod
from datetime import datetime, timedelta

class VipMixin():
    def show_vip_benefits(self):
        print("Maximum 5 borrowed books")
        print("30-day borrowing period")

class Customer(ABC):
    def __init__(self,name,id):
        self.name = name
        self.id = id

    @abstractmethod
    def Maximum_number_books(self):
        pass
    @abstractmethod
    def borrow_duration(self):
        pass


class NormalCustomer(Customer):
    def Maximum_number_books(self):
        return 3
    def borrow_duration(self):
        return 15

class VipCustomer(Customer,VipMixin):
    def Maximum_number_books(self):
        return 5
    def borrow_duration(self):
        return 30

#-----------Book----------
class Book:
    def __init__(self,id_book,title,author):
        self.id_book = id_book
        self.title = title
        self.author = author
        self.shelf = None
        self._borrowing_status = False


#---------Shelf----------
class Shelf:
    def __init__(self,id_shelf,capacity):
        self.id_shelf = id_shelf
        self.capacity = capacity
        self.books = []
    def __iter__(self):
        return iter(self.books)    
    def __len__(self):
        return len(self.books)

#--------Boroowing--------


class Borrowing:
    def __init__(self, book, customer, borrow_date, return_date):
        self.book = book
        self.customer = customer
        self.borrow_date = borrow_date
        self.return_date = return_date

    @property
    def is_overdue(self):
        return datetime.now() > self.return_date


#----------library--------
class Library():
    def __init__(self):
        self.normal_customers = []
        self.vip_customers = []
        self.books = []
        self.shelves = []
        self.borrowings = []

    def add_customer(self, customer):
        if not isinstance(customer, Customer):
            raise ValueError("Invalid customer")
        for i in self.normal_customers:
            if i.id == customer.id:
                raise ValueError("Customer ID already exists")
        for i in self.vip_customers:
            if i.id == customer.id:
                raise ValueError("Customer ID already exists")
        if isinstance(customer, NormalCustomer):
            self.normal_customers.append(customer)
        elif isinstance(customer, VipCustomer):
            self.vip_customers.append(customer)

    def del_customer(self, customer_id):

        for i in self.normal_customers:
            if i.id == customer_id:
                self.normal_customers.remove(i)
                return

        for i in self.vip_customers:
            if i.id == customer_id:
                self.vip_customers.remove(i)
                return
        raise ValueError("Customer does not exist")

    def add_book(self, book):
        if not isinstance(book, Book):
            raise ValueError("Invalid book")

        for b in self.books:
            if b.id_book == book.id_book:
                raise ValueError("Book ID already exists")
        self.books.append(book)

    def del_book(self, book_id):
        for b in self.books:
            if b.id_book == book_id:
                self.books.remove(b)
                return
        raise ValueError("Book does not exist")

    def creating_shelf(self, id_shelf, capacity):
        for shelf in self.shelves:
            if shelf.id_shelf == id_shelf:
                raise ValueError("Shelf ID already exists")

        new_shelf = Shelf(id_shelf, capacity)
        self.shelves.append(new_shelf)


    def placing(self, book_id, shelf_id):
        book = None
        shelf = None

        for b in self.books:
            if b.id_book == book_id:
                book = b
                break

        for s in self.shelves:
            if s.id_shelf == shelf_id:
                shelf = s
                break

        if book is None:
            raise ValueError("Book does not exist")

        if shelf is None:
            raise ValueError("Shelf does not exist")

        if len(shelf) >= shelf.capacity:
            raise ValueError("Shelf is full")

        if book in shelf.books:
            raise ValueError("Book is already on this shelf")

        shelf.books.append(book)
        book.shelf = shelf


    def borrowing(self, book_id, customer_id):
        book = None
        customer = None

        for b in self.books:
            if b.id_book == book_id:
                book = b
                break

        for c in self.normal_customers:
            if c.id == customer_id:
                customer = c
                break

        if customer is None:
            for c in self.vip_customers:
                if c.id == customer_id:
                    customer = c
                    break

        if book is None:
            raise ValueError("Book does not exist")

        if customer is None:
            raise ValueError("Customer does not exist")

        if book._borrowing_status:
            raise ValueError("Book is already borrowed")

        customer_borrowings = 0

        for borrowing in self.borrowings:
            if borrowing.customer.id == customer.id:
                customer_borrowings += 1

        if customer_borrowings >= customer.Maximum_number_books():
            raise ValueError("Customer reached borrowing limit")

        borrow_date = datetime.now()
        return_date = borrow_date + timedelta(days=customer.borrow_duration())

        new_borrowing = Borrowing(book, customer, borrow_date, return_date)
        self.borrowings.append(new_borrowing)

        book._borrowing_status = True


    def return_book(self, book_id):
        for borrowing in self.borrowings:
            if borrowing.book.id_book == book_id:

                if not borrowing.book._borrowing_status:
                    raise ValueError("Book is already returned")

                borrowing.book._borrowing_status = False
                self.borrowings.remove(borrowing)

                return

        raise ValueError("Borrowing does not exist")