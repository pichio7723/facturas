from fastapi import APIRouter, HTTPException
from models.venta import Venta, VentaCrear
from models.factura import Factura
import state

router = APIRouter()

@router.post("/venta")
async def venta_de_producto(venta: VentaCrear):
    # Buscar cliente
    cliente = next(
        (u for u in state.usuarios if u.id == venta.cliente_id),
        None
    )
    if cliente is None:
        raise HTTPException(
            status_code=404,
            detail="Cliente no encontrado"
        )

    # Buscar producto
    producto = next(
        (p for p in state.productos if p.id == venta.producto_id),
        None
    )
    if producto is None:
        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado"
        )

    # Verificar stock
    if venta.cantidad > producto.stock:
        raise HTTPException(
            status_code=400,
            detail="Stock insuficiente"
        )

    # Descontar stock y calcular subtotal
    producto.stock -= venta.cantidad
    subtotal = producto.precio * venta.cantidad

    # Crear venta
    nueva_venta = Venta(
        producto_id=producto.id,
        cantidad=venta.cantidad,
        subtotal=subtotal
    )

    # Generar factura
    state.ultimo_id_factura += 1
    nueva_factura = Factura(
        id=state.ultimo_id_factura,
        cliente_id=cliente.id,
        ventas=[nueva_venta],
        total=subtotal
    )

    state.facturas.append(nueva_factura)
    return {
        "mensaje": "Compra realizada exitosamente",
        "factura": nueva_factura
    }

@router.get("/facturas/{id}")
async def listar_factura(id: int):
    facturas_cliente = [
        factura for factura in state.facturas
        if factura.cliente_id == id
    ]
    if not facturas_cliente:
        raise HTTPException(
            status_code=404,
            detail="No se encontraron facturas para este cliente"
        )
    return facturas_cliente