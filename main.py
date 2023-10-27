from fastapi import FastAPI

from api.shopApi import shop_router
from db import engine, Base

app = FastAPI()
v1 = FastAPI()

Base.metadata.create_all(bind=engine)
app.include_router(router=shop_router)


