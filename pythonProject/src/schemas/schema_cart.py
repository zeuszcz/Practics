from pydantic import BaseModel


class CartCreate(BaseModel):
    name: str
    sum: int