from pydantic import BaseModel


class ServiceCreate(BaseModel):
    cost: int
    name: str


class ServiceUpdate(BaseModel):
    cost: int
    name: str



class ServiceDelete(BaseModel):
    cost: int
    name: str



class ServiceRead(BaseModel):
    id:int
    cost: int
    name: str