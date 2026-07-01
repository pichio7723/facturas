from fastapi import APIRouter, HTTPException
from models.cliente import clienteCrear, cliente, clienteEditar
import database

router = APIRouter()

@router.post("/usuarioCrear")
def crear_usuario(usuario: clienteCrear):
    database.ultimo_id += 1
    cliente_nuevo = cliente(
        id=database.ultimo_id,
        **usuario.model_dump()
    )
    database.usuarios.append(cliente_nuevo)
    return {
        "mensaje": "usuario creado exitosamente",
        "usuario": cliente_nuevo
    }

@router.get("/usuarios")
async def listar_todos():
    if not database.usuarios:
        raise HTTPException(
            status_code=404,
            detail="No hay usuarios registrados."
        )
    return database.usuarios

@router.delete("/Udelete/{id}")
async def borrar_usuario(id: int):
    for U in database.usuarios:
        if U.id == id:
            database.usuarios.remove(U)
            return {"mensaje": "Usuario eliminado"}
    raise HTTPException(
        status_code=404,
        detail="Usuario no encontrado"
    )

@router.put("/Ueditar/{id}")
async def editar_usuario(id: int, usuario: clienteEditar):
    for U in database.usuarios:
        if U.id == id:
            for key, value in usuario.model_dump(exclude_unset=True).items():
                    setattr(U, key, value)
            return {"mensaje": "Usuario actualizado", "usuario": U}
    raise HTTPException(
        status_code=404,
        detail="Usuario no encontrado"
    )