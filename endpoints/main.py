from fastapi import FastAPI
import asyncio
from models.cliente import clienteBase, clienteCrear, clienteEditar, cliente
from models.productos import Producto
from fastapi import HTTPException

app = FastAPI()


productos = [
    Producto(id=1, nombre="Teclado", precio=120000, stock=10),
    Producto(id=2, nombre="Mouse", precio=50000, stock=20),
    Producto(id=3, nombre="Monitor", precio=800000, stock=5),
]
usuarios = []
ultimo_id = 0

@app.post("/usuarioCrear")
def crear_usuario(usuario : clienteCrear):
    global ultimo_id
    ultimo_id += 1
    #definicion de cliente
    cliente_nuevo = cliente(
        id = ultimo_id,
        **usuario.model_dump()
    )
    usuarios.append(cliente_nuevo)

    return {
        "mensaje" : "usuario creado exitosamente",
        "usuario" : cliente_nuevo
    }


@app.get("/usuarios")
async def listar_todos():
    if not usuarios:
        raise HTTPException(
            status_code=404,
            detail="No hay usuarios registrados."
        )
    return usuarios




