from pydantic import BaseModel
from typing import Optional


class Address(BaseModel):
    street: str
    city: str
    postal_code: str


class Company(BaseModel):
    name: str
    address: Optional[Address] = None


class Employee(BaseModel):
    name: str
    company: Optional[Company] = None


user_data = {
    "name": "Vijay Jadon",
    "company": {
        "name": "Google",
        "address": {"street": "ST Marg", "city": "Gwalior", "postal_code": "120011"},
    },
}

user = Employee(**user_data)
print(user)
