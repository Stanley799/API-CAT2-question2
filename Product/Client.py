#has the script for client interaction 

import requests

BASE_URL = "http://127.0.0.1:5000"

# Add a new product
def add_product(name, description, price):
    data = {
        "name": name,
        "description": description,
        "price": price
    }
    response = requests.post(f"{BASE_URL}/products", json=data)
    print(response.status_code, response.json())

# Retrieve all products
def get_products():
    response = requests.get(f"{BASE_URL}/products")
    print(response.status_code, response.json())

# Example usage
if __name__ == "__main__":
    add_product("Laptop", "High-performance laptop", 1200.99)
    add_product("Phone", "Latest smartphone", 899.49)
    get_products()
