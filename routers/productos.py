from fastapi import APIRouter, HTTPException
from models.productos import Producto
import database

router = APIRouter()

@router.get("/productos")
async def listar_productos():
    if not database.productos:
        raise HTTPException(
            status_code=404,
            detail="No hay productos disponibles."
        )
    return database.productos