from pydantic import BaseModel, computed_field, Field


class Product(BaseModel):
    price: float
    quantity: int

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity


product_data = {"price": 12.04, "quantity": 4}

product1 = Product(**product_data)
print(product1.total_price)
print(type(product1.total_price))
