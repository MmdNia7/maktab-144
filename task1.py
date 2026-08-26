class Book:
    total_books = 0

    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        Book.total_books += 1

    def apply_discount(self, percent):
        self.price -= self.price * (percent / 100)
        return self.price

    @classmethod
    def get_total_books(cls):
        return cls.total_books

    @staticmethod
    def is_expensive(price):
        return price > 200_000

    def print_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")
        print(f"Price: {self.price}")


book1 = Book("Python Basics", "Ali Ahmadi", 250, 300_000)
book2 = Book("Clean Code", "Robert Martin", 450, 500_000)
book3 = Book("Data Science", "Sara Mohammadi", 320, 180_000)

new_price = book1.apply_discount(20)
print("New price after discount:", new_price)

print("Total books:", Book.get_total_books())

print(Book.is_expensive(350_000))

book1.print_info()
