from database import engine, Base

# importar todos los modelos para que Base los registre
from models.db.cliente import Cliente
from models.db.productos import Producto
from models.db.venta import Venta
from models.db.factura import Factura

Base.metadata.create_all(bind=engine)
print("Un mago nunca llega tarde, Frodo Bolsón, ni pronto. Llega exactamente cuando se lo propone")