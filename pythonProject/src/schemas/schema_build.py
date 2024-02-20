from pydantic import BaseModel


class BuildCreate(BaseModel):
    id:int
    product_id:int
    product_component_id:int
    name: str