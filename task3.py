#3
products = [
{"name": "Keyboard", "price": 500000, "in_stock": True},
{"name": "Mouse", "price": 200000, "in_stock": False},
{"name": "Monitor", "price": 3500000, "in_stock": True},
{"name": "Webcam", "price": 800000, "in_stock": True},
]
from functools import reduce
in_stock = list(filter(lambda i:i["in_stock"] == True,products))
b = list(map(lambda i:(i["name"],i["price"]*0.9),in_stock))
c = reduce(lambda x,y:x+y[1],b,0)
for name,price in b:
    print(f"{name}: {price:.2f}")
print(f"sum price: {c:.2f}")