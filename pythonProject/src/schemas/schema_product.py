from pydantic import BaseModel


class ProductCreate(BaseModel):
    id:int
    cost: int
    name: str