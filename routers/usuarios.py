from fastapi import APIRouter, HTTPException
from models.cliente import clienteCrear, cliente
import state

router = APIRouter()

@router.post("/usuarioCrear")
def crear_usuario(usuario: clienteCrear):
    state.ultimo_id += 1
    cliente_nuevo = cliente(
        id=state.ultimo_id,
        **usuario.model_dump()
    )
    state.usuarios.append(cliente_nuevo)
    return {
        "mensaje": "usuario creado exitosamente",
        "usuario": cliente_nuevo
    }

@router.get("/usuarios")
async def listar_todos():
    if not state.usuarios:
        raise HTTPException(
            status_code=404,
            detail="No hay usuarios registrados."
        )
    return state.usuarios

@router.delete("/Udelete/{id}")
async def borrar_usuario(id: int):
    for U in state.usuarios:
        if U.id == id:
            state.usuarios.remove(U)
            return {"mensaje": "Usuario eliminado"}
    raise HTTPException(
        status_code=404,
        detail="Usuario no encontrado"
    )