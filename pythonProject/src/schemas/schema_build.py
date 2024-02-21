from pydantic import BaseModel


class BuildCreate(BaseModel):
    product_id:int
    product_component_id:int
    name: str


class BuildUpdate(BaseModel):
    product_id:int
    product_component_id:int
    name: str


class BuildDelete(BaseModel):
    name: str



class BuildRead(BaseModel):
    id:int
    product_id:int
    product_component_id:int
    name: str