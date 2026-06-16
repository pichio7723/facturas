from pydantic import BaseModel

class ProductoBase(BaseModel):
    nombre: str
    precio: float
    stock: int

class ProductoCrear(ProductoBase):
    pass

class Producto(ProductoBase):
    id: int