from pydantic import BaseModel
from typing import List, Dict, Optional


class Cart(BaseModel):
    user_id: int
    items: List[str]
    quantities: Dict[str, int]


class BlogPost(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None


cart_data = {
    "user_id": 123,
    "items": ["mouse", "cpu", "printer", "keyboard"],
    "quantities": {"mouse": 2, "cpu": 3, "printer": 4, "keyboard": 1},
}

order = Cart(**cart_data)
print(order)
