import requests
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

# try:
#     responce1 = requests.get("https://dummyjson.com/users")

#     responce1.raise_for_status()

#     users = responce1.json()

#     for user in users["users"]:
#         print(user["firstName"],user["lastName"],user["age"],user["email"])

#     logging.info("Users received successfully")
    
# except requests.exceptions.RequestException as e:
#     logging.error(e)


# try:
#     responce2 = requests.get("https://dummyjson.com/users/5")

#     responce2.raise_for_status()

#     user = responce2.json()

#     print(user["firstName"] , user["lastName"], user["age"], user["email"])

#     logging.info("Users received successfully")

# except requests.exceptions.RequestException as e:
#     logging.error(e)


try:
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    age = int(input("Enter Age: "))
    email = input("Enter Email: ")
    username = input("Enter Username: ")

    new_user = {
        "firstName": first_name,
        "lastName": last_name,
        "age": age,
        "email": email,
        "username": username
    }

    response3 = requests.post(
        "https://dummyjson.com/users/add",
        json=new_user
    )

    response3.raise_for_status()

    result = response3.json()
    print(result)

    print("ID:", result["id"])
    print("First Name:", result["firstName"])
    print("Last Name:", result["lastName"])
    print("Age: ", result["age"])
    print("Email:", result["email"])
    print("Username:", result["username"])

    logging.info("User added successfully")

except (requests.exceptions.RequestException, ValueError) as e:
    logging.error(e)