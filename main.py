from fastapi import FastAPI
from models import Product
app = FastAPI()

@app.get("/")
def greet():
    return "Hello, World!"

products = [
    Product(id=1, name="Laptop", description="A high-performance laptop", price=999.99, quantity=10),
    Product(id=2, name="Smartphone", description="A powerful smartphone", price=499.99, quantity=20),
    Product(id=3, name="Headphones", description="Noise-cancelling headphones", price=199.99, quantity=15),
    Product(id=4, name="Smartwatch", description="A stylish smartwatch", price=299.99, quantity=5),
    Product(id=5, name="Tablet", description="A versatile tablet", price=399.99, quantity=8),
    Product(id=6, name="Camera", description="A high-resolution camera", price=599.99, quantity=12)

]
@app.get("/products")
def get_products():
    return products

@app.get("/products/{product_id}")
def get_product_by_id(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
    return {"error": "Product not found"}

@app.post("/products")
def create_product(product: Product):
    products.append(product)
    return product

@app.put("/products/{product_id}")
def update_product(product_id: int, product: Product):
    for i in range(len(products)):
        if products[i].id == product_id:
            products[i] = product
            return product
    return {"error": "Product not found"}    


@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for i in range (len(products)):
        if products[i].id == product_id:
            del products[i]
            return {"message": "Product deleted"}
    return {"error": "Product not found"}
