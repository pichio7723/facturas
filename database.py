from models.cliente import cliente
from models.productos import Producto
from models.factura import Factura

# Usuarios
usuarios: list[cliente] = []
ultimo_id: int = 0

# Productos
productos: list[Producto] = [
    Producto(id=1, nombre="Teclado", precio=120000, stock=10),
    Producto(id=2, nombre="Mouse", precio=50000, stock=20),
    Producto(id=3, nombre="Monitor", precio=800000, stock=5),
]

# Facturas
facturas: list[Factura] = []
ultimo_id_factura: int = 0