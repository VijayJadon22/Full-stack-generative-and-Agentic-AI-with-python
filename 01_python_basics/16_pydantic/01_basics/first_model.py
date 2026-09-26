from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    isActive: bool


input_data = {"id": 1, "name": "vijay", "isActive": True}

user = User(**input_data)
print(user)
