from pydantic import BaseModel
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class clienteBase(DeclarativeBase):
    __tablename__ = "clientes"
    nombre : Mapped[str] = mapped_column()
    edad : Mapped[int] = mapped_column()
    saldo : Mapped[int] = mapped_column()

class clienteCrear(clienteBase):
    pass

class clienteEditar(clienteBase):
    nombre: str | None = None
    edad: int | None = None

class cliente(clienteBase):
    id: Mapped[int] = mapped_column(primary_key=True)