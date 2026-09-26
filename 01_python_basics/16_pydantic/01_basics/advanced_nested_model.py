from pydantic import BaseModel
from typing import Optional, List, Union


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


# user_data = {
#     "name": "Vijay Jadon",
#     "company": {
#         "name": "Google",
#         "address": {"street": "ST Marg", "city": "Gwalior", "postal_code": "120011"},
#     },
# }

# user = Employee(**user_data)
# print(user)

# user = Employee(
#     name="Vijay Jadon",
#     company=Company(
#         name="Google",
#         address=Address(street="ST Marg", city="Gwalior", postal_code="120011"),
#     ),
# )

# print(user)


class TextContent(BaseModel):
    type: str = "text"
    content: str


class ImageContent(BaseModel):
    type: str = "Image"
    url: str
    alt_text: str


class Article(BaseModel):
    title: str
    sections: List[Union[TextContent, ImageContent]]


article1 = Article(
    title="CJP Protest Restarts",
    sections=[
        TextContent(
            type="Para about the protest", content="Detailed para about the protest"
        ),
        ImageContent(
            type="Image uploaded",
            url="https://example.com",
            alt_text="Image related to article",
        ),
    ],
)

print(article1)


class Country(BaseModel):
    name: str
    code: str


class State(BaseModel):
    name: str
    country: Country


class City(BaseModel):
    name: str
    state: State


class Address(BaseModel):
    street: str
    city: City
    postal_code: str


class Organization(BaseModel):
    name: str
    head_quarter: Address
    branches: List[Address] = []
