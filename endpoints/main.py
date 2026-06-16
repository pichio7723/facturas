#importacion tecnica
from fastapi import FastAPI
import asyncio
from fastapi import HTTPException


#importacion de modulos
from models.cliente import clienteBase, clienteCrear, clienteEditar, cliente
from models.productos import Producto
from models.venta import Venta,VentaCrear
from models.factura import Factura

app = FastAPI()


productos = [
    Producto(id=1, nombre="Teclado", precio=120000, stock=10),
    Producto(id=2, nombre="Mouse", precio=50000, stock=20),
    Producto(id=3, nombre="Monitor", precio=800000, stock=5),
]
usuarios = []
facturas = []
ultimo_id = 0
ultimo_id_factura = 0

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


@app.post("/venta")
async def venta_de_producto(venta: VentaCrear):
    global ultimo_id_factura

    # Buscar cliente
    cliente = next(
        (u for u in usuarios if u.id == venta.cliente_id),
        None
    )

    if cliente is None:
        raise HTTPException(
            status_code=404,
            detail="Cliente no encontrado"
        )

    # Buscar producto
    producto = next(
        (p for p in productos if p.id == venta.producto_id),
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

    # Descontar stock
    producto.stock -= venta.cantidad

    # Calcular subtotal
    subtotal = producto.precio * venta.cantidad

    # Crear la venta
    nueva_venta = Venta(
        producto_id=producto.id,
        cantidad=venta.cantidad,
        subtotal=subtotal
    )

    # Generar la factura
    ultimo_id_factura += 1

    nueva_factura = Factura(
        id=ultimo_id_factura,
        cliente_id=cliente.id,
        ventas=[nueva_venta],
        total=subtotal
    )

    # Guardar factura
    facturas.append(nueva_factura)

    return {
        "mensaje": "Compra realizada exitosamente",
        "factura": nueva_factura
    }

@app.get("/facturas/{id}")
async def listar_factura(id: int):
    return [
        factura
        for factura in facturas
        if factura.cliente_id == id
    ]