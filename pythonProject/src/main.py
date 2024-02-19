from fastapi import FastAPI


from src.router import router as router_cart
from src.routercomponent import router as router_component
from src.routerproduct import router as router_product
from src.router_cart_item import router as router_cart_item
from src.router_service import router as router_service

app = FastAPI(
    title="calculator"
)


app.include_router(router_cart)
app.include_router(router_component)
app.include_router(router_product)
app.include_router(router_cart_item)
app.include_router(router_service)