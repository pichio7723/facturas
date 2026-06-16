from pydantic import BaseModel
from .venta import Venta

class Factura(BaseModel):
    id: int
    cliente_id: int
    ventas: list[Venta]
    total: float