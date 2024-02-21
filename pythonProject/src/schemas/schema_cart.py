from pydantic import BaseModel


class CartCreate(BaseModel):
    name: str
    sum: int



class CartUpdate(BaseModel):
    name: str
    sum: int


class CartDelete(BaseModel):
    name: str
    sum: int

class CartRead(BaseModel):
    id: int
    name: str
    sum: int