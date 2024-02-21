from pydantic import BaseModel


class ProductTypeCreate(BaseModel):
    name: str


class ProductTypeUpdate(BaseModel):
    name: str



class ProductTypeDelete(BaseModel):
    name: str

class ProductTypeRead(BaseModel):
    id: int
    name: str
