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


class Booking(BaseModel):
    user_id: int
    room_id: int
    nights: int = Field(..., ge=1)
    rate_per_night: float

    @computed_field
    @property
    def total_bill(self) -> float:
        return self.nights * self.rate_per_night


booking = Booking(user_id=1, room_id=143, nights=2, rate_per_night=120.4)
print(booking.total_bill)
print(booking.model_dump())
