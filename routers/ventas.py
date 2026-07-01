from fastapi import APIRouter, HTTPException
from models.venta import Venta, VentaCrear
from models.factura import Factura
import database

router = APIRouter()

@router.post("/venta")
async def venta_de_producto(venta: VentaCrear):
    # Buscar cliente
    cliente = next(
        (u for u in database.usuarios if u.id == venta.cliente_id),
        None
    )
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")

    # Buscar producto
    producto = next(
        (p for p in database.productos if p.id == venta.producto_id),
        None
    )
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    # Verificar stock
    if venta.cantidad > producto.stock:
        raise HTTPException(status_code=400, detail="Stock insuficiente")

    # Calcular subtotal
    subtotal = producto.precio * venta.cantidad

    # Verificar saldo
    if cliente.saldo < subtotal:
        raise HTTPException(
            status_code=400,
            detail=f"Saldo insuficiente. Saldo actual: {cliente.saldo}, Total a pagar: {subtotal}"
        )

    # Descontar stock y saldo
    producto.stock -= venta.cantidad
    cliente.saldo -= subtotal

    # Crear venta
    nueva_venta = Venta(
        producto_id=producto.id,
        cantidad=venta.cantidad,
        subtotal=subtotal #lo que el cliente gasto, es importante para no confundirse con lo que le sobra
    )

    # Generar factura
    database.ultimo_id_factura += 1
    nueva_factura = Factura(
        id=database.ultimo_id_factura,
        cliente_id=cliente.id,
        nombre_cliente=cliente.nombre,
        ventas=[nueva_venta],
        cambio=cliente.saldo,
        total=subtotal
    )

    database.facturas.append(nueva_factura)
    return {
        "mensaje": "Compra realizada exitosamente",
        "factura": nueva_factura
    }

@router.get("/facturas")
async def listar_facturas():
    if not database.facturas:
        raise HTTPException(status_code=404, detail="No hay facturas registradas.")
    return database.facturas

@router.get("/facturas/{id}")
async def listar_factura(id: int):
    facturas_cliente = [
        factura for factura in database.facturas
        if factura.cliente_id == id
    ]
    if not facturas_cliente:
        raise HTTPException(status_code=404, detail="No se encontraron facturas para este cliente")
    return facturas_cliente

@router.delete("/facturas/{id}")
async def eliminar_factura(id: int):
    for factura in database.facturas:
        if factura.id == id:
            database.facturas.remove(factura)
            return {"mensaje": "Factura eliminada"}
    raise HTTPException(status_code=404, detail="Factura no encontrada")