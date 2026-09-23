from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True


product_one = Product(id=1, name="Laptop", price=68.98, in_stock=True)
product_two = Product(id=2, name="Mouse", price=23.48)
print(product_one)
print(product_two)
# product_three = Product(id=4) #this will give error as required fields are required we can skip the default value fields that wont give error
