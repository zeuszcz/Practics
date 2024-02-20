from pydantic import BaseModel


class ProductTypeCreate(BaseModel):
    id:int
    name: str