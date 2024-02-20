from pydantic import BaseModel


class ProductComponentCreate(BaseModel):
    id:int
    product_type_id:int
    name: str
    cost: int