from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from database import Base
from models.db.venta import Venta

class Factura(Base):
    __tablename__ = "facturas"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    cliente_id: Mapped[int] = mapped_column(ForeignKey("clientes.id"))
    nombre_cliente: Mapped[str]
    total: Mapped[float]
    cambio: Mapped[float]
    ventas: Mapped[list[Venta]] = relationship("Venta", lazy="joined")