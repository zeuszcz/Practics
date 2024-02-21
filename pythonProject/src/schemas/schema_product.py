from pydantic import BaseModel


class ProductCreate(BaseModel):
    cost: int
    name: str


class ProductUpdate(BaseModel):
    cost: int
    name: str


class ProductDelete(BaseModel):
    name: str



class ProductRead(BaseModel):
    id:int
    cost: int
    name: str