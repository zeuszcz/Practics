from pydantic import BaseModel


class CartItemCreate(BaseModel):
    id:int
    cart_id: int
    product_id: int
    service_id: int