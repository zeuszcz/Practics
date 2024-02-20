from pydantic import BaseModel


class ServiceCreate(BaseModel):
    id:int
    cost: int
    name: str