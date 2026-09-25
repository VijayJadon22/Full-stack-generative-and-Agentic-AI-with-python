from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime


class Address(BaseModel):
    street: str
    city: str
    pin_code: str


class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    created_at: datetime
    address: Address
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime("%d-%m-%Y %H:%M:%S")}
    )


user = User(
    id=1,
    name="Vijay Jadon",
    email="john@gmail.com",
    created_at=datetime(2026, 9, 25, 18, 9),
    address=Address(street="ST Road", city="Gwalior", pin_code="474023"),
    tags=["premium", "subscriber"],
)

python_dict = user.model_dump()
print(python_dict)

json_str = user.model_dump_json()
print(json_str)
