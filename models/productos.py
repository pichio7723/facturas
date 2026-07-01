from pydantic import BaseModel
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class ProductoBase(BaseModel):
    nombre: str
    precio: float
    stock: int

class ProductoCrear(ProductoBase):
    pass

class Producto(ProductoBase):
    id: int