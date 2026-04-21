from fastapi import FastAPI
from models import Product
app = FastAPI()

@app.get("/")
def greet():
    return "Hello, World!"

products = [
    Product(1, "Laptop", "A high-performance laptop", 999.99, 10),
    Product(2, "Smartphone", "A latest model smartphone", 499.99, 20)
]
@app.get("/products")
def get_products():
    return products