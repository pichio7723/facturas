from pydantic import BaseModel

class clienteBase(BaseModel):
    nombre : str
    edad : int
    saldo : int

class clienteCrear(clienteBase):
    pass

class clienteEditar(clienteBase):
    nombre: str | None = None
    edad: int | None = None

class cliente(clienteBase):
    id : int | None = None