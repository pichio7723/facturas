from pydantic import BaseModel
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class VentaCrear(BaseModel):
    cliente_id: int
    producto_id: int
    cantidad: int


class Venta(BaseModel):
    producto_id: int
    cantidad: int
    subtotal: float