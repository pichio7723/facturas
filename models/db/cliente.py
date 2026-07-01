from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class Cliente(Base):
    __tablename__ = "clientes"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str]
    edad: Mapped[int]
    saldo: Mapped[int]