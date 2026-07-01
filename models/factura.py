from pydantic import BaseModel
from .venta import Venta
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Factura(BaseModel):
    id: int
    cliente_id: int
    nombre_cliente: str
    ventas: list[Venta]
    total: float
    cambio: float