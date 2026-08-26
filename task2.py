class Product:
    store_name = "ShopHub"
    increase_rate = 1.05
    def __init__(self, title, category, price):
        self.title = title
        self.category = category
        self.price = price
    def full_label(self):
        return f"{self.title} ({self.category})"
    def apply_increase(self):
        self.price *= Product.increase_rate
    @classmethod
    def set_increase_rate(cls, new_rate):
        cls.increase_rate = new_rate
    @classmethod
    def from_string(cls, product_string):
        title, category, price = product_string.split("-")
        return cls(title, category, float(price))
    @staticmethod
    def is_open(day):
        return day != "friday"

product1 = Product("Laptop", "Digital", 8000)
product2 = Product.from_string("Phone-Digital-5000")
print(product1.full_label())     
print(product2.full_label())  

print("Price before increase:", product1.price)
product1.apply_increase()
print("Price after increase:", product1.price)

Product.set_increase_rate(1.10)

product1.apply_increase()
print("Price after second increase:", product1.price)

print(Product.is_open("friday"))   
print(Product.is_open("monday"))   