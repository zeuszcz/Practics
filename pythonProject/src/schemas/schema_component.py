from pydantic import BaseModel


class ComponentCreate(BaseModel):
    product_type_id:int
    name: str
    cost: int


class ComponentUpdate(BaseModel):
    product_type_id:int
    name: str
    cost: int


class ComponentDelete(BaseModel):
    product_type_id:int
    name: str
    cost: int


class ComponentRead(BaseModel):
    id:int
    product_type_id:int
    name: str
    cost: int