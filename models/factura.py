from pydantic import BaseModel
from .venta import Venta

class Factura(BaseModel):
    id: int
    cliente_id: int
    nombre_cliente: str
    ventas: list[Venta]
    total: float