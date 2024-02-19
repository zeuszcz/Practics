from sqlalchemy import Table, Column, MetaData, Integer, String, ForeignKey
from pydantic import BaseModel

TableMetaData = MetaData()

cart = Table(
    "cart",
    TableMetaData,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("sum", Integer)
)

class CartCreate(BaseModel):
    name: str
    sum: int

service = Table(
    "service",
    TableMetaData,
    Column("id", Integer, primary_key=True),
    Column("cost", Integer, nullable=False),
    Column("name", String, nullable=False),

)
class ServiceCreate(BaseModel):
    id:int
    cost: int
    name: str


product = Table(
    "product",
    TableMetaData,
    Column("id",Integer,primary_key=True),
    Column("cost",Integer,nullable=False),
    Column("name",String,nullable=False),

)

class ProductCreate(BaseModel):
    id:int
    cost: int
    name: str

cart_item = Table(
    "cart_item",
    TableMetaData,
    Column("id", Integer, primary_key=True),
    Column("cart_id", Integer,ForeignKey("cart.id")),
    Column("product_id", Integer,ForeignKey("product.id")),
    Column("servece_id",Integer,ForeignKey("service.id")),

)

class CartItemCreate(BaseModel):
    id:int
    cart_id: int
    product_id: int
    service_id: int

product_type = Table(
    "product_type",
    TableMetaData,
    Column("id",Integer,primary_key=True),
    Column("name",String,nullable=False),

)

class ProductTypeCreate(BaseModel):
    id:int
    name: str


product_component = Table(
    "product_component",
    TableMetaData,
    Column("id",Integer,primary_key=True),
    Column("product_type_id",Integer,ForeignKey("product_type.id")),
    Column("name",String,nullable=False),
    Column("cost",Integer,nullable=False),

)

class ProductComponentCreate(BaseModel):
    id:int
    product_type_id:int
    name: str
    cost: int

build = Table(
    "build",
    TableMetaData,
    Column("id",Integer,primary_key=True),
    Column("product_id",Integer,ForeignKey("product.id")),
    Column("product_component_id",Integer,ForeignKey("product_component.id")),
    Column("name",String,nullable=False),

)

class BuildCreate(BaseModel):
    id:int
    product_id:int
    product_component_id:int
    name: str
