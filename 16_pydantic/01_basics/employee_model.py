from pydantic import BaseModel, Field
from typing import Optional
import re


class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=4,
        max_length=12,
        description="Name as string",
        examples="Vijay Jadon",
    )
    department: Optional[str] = "General"
    salary: float = Field(
        ...,
        ge=10000,
        lt=200000,
        description="Annual Salary In INR",
    )


# class User(BaseModel):
#     email: str = Field(..., regex=r"")
#     phone: str = Field(..., regex=r"")
#     age: int = Field(..., ge=0, lt=120, description="Age in Years")
#     discount: float = Field(..., ge=0, le=100, description="Discount in percentage")


user_data = {"id": 123, "name": "Vijay Jadon", "salary": 40000}
user = Employee(**user_data)
print(user)
