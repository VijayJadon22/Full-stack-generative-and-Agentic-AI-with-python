from typing import List, Optional
from pydantic import BaseModel


class Address(BaseModel):
    street: str
    city: str
    postal_code: str


class User(BaseModel):
    id: int
    name: str
    address: Address

#First way of accessing the Models
address = Address(street="ST Marg", city="Gwalior", postal_code="121001")
user = User(id=12, name="Vijay Jadon", address=address)

print(user)
