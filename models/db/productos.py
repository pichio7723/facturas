from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class Producto(Base):
    __tablename__ = "productos"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str]
    precio: Mapped[float]
    stock: Mapped[int]