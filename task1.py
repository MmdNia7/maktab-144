import requests
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)


try:
    response = requests.get("https://dummyjson.com/products")
    response.raise_for_status()

    products = response.json()

    for product in products["products"]:
        print(product["title"], product["price"], product["category"])

    logging.info("Products received successfully")

except requests.exceptions.RequestException as e:
    logging.error(e)
# except Exception as e:
#     logging.error(e)

print("*"*30)
print("*"*30)
print("*"*30)


try:
    response2 = requests.get("https://dummyjson.com/products/1")
    response2.raise_for_status()

    products2 = response2.json()
    
    print(products2["title"], products2["price"], products2["category"])

    logging.info("Product received successfully")

except requests.exceptions.RequestException as e:
    logging.error(e)


print("*"*30)
print("*"*30)
print("*"*30)


new_dict = {
    "title": input("Input title: "),
    "description": input("Input description: "),
    "price": float(input("Input price: ")),
    "category": input("Input category: ")
}

try:
    response_3 = requests.post(
        "https://dummyjson.com/products/add",
        json=new_dict
    )

    response_3.raise_for_status()

    product = response_3.json()

    logging.info("Product added successfully")

    print("Product ID:", product["id"])
    print("Title:", product["title"])
    print("Price:", product["price"])
    print("Category:", product["category"])

except requests.exceptions.RequestException as e:
    logging.error(e)
