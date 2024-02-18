from fastapi import FastAPI


from src.router import router as router_cart
from src.routercomponent import router as router_component
from src.routerproduct import router as router_product

app = FastAPI(
    title="calculator"
)


app.include_router(router_cart)
app.include_router(router_component)
app.include_router(router_product)
