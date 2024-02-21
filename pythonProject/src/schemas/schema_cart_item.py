from pydantic import BaseModel


class CartItemCreate(BaseModel):
    cart_id: int
    product_id: int
    service_id: int


class CartItemUpdate(BaseModel):
    cart_id: int
    product_id: int
    service_id: int


class CartItemRead(BaseModel):
    id:int
    cart_id: int
    product_id: int
    service_id: int


class CartItemDelete(BaseModel):
    cart_id: int
    product_id: int
    service_id: int