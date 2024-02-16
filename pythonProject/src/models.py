from sqlalchemy import Table, JSON, Column, MetaData, Integer, String, TIMESTAMP, ForeignKey

TableMetaData = MetaData()

cart = Table(
    "cart",
    TableMetaData,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("sum", Integer)
)

service = Table(
    "service",
    TableMetaData,
    Column("id", Integer, primary_key=True),
    Column("cost", Integer, nullable=False),
    Column("name", String, nullable=False),

)


product = Table(
    "product",
    TableMetaData,
    Column("id",Integer,primary_key=True),
    Column("cost",Integer,nullable=False),
    Column("name",String,nullable=False),

)


cart_item = Table(
    "cart_item",
    TableMetaData,
    Column("id", Integer, primary_key=True),
    Column("cart_id", Integer,ForeignKey = "cart.id"),
    Column("product_id", Integer,ForeignKey="product.id"),
    Column("servece_id",Integer,ForeignKey="service.id"),

)


product_type = Table(
    "product_type",
    TableMetaData,
    Column("id",Integer,primary_key=True),
    Column("name",String,nullable=False),

)

product_component = Table(
    "product_component",
    TableMetaData,
    Column("id",Integer,primary_key=True),
    Column("product_type_id",Integer,ForeignKey="product_type.id"),
    Column("name",String,nullable=False),
    Column("cost",Integer,nullable=False),

)

build = Table(
    "build",
    TableMetaData,
    Column("id",Integer,primary_key=True),
    Column("product_id",Integer,ForeignKey = "product.id"),
    Column("product_component_id",Integer,ForeignKey="product_component.id"),
    Column("name",String,nullable=False),

)