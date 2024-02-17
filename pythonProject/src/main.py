from fastapi import FastAPI


from router import router as router_cart

app = FastAPI(
    title="calculator"
)


app.include_router(router_cart)
