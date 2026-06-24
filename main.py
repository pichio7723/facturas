from fastapi import FastAPI
from routers import usuarios, ventas, productos

app = FastAPI()

app.include_router(usuarios.router)
app.include_router(ventas.router)
app.include_router(productos.router)