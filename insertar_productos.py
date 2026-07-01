from database import SessionLocal
from models.db.productos import Producto

db = SessionLocal()

productos = [
    Producto(nombre="Teclado", precio=120000, stock=10),
    Producto(nombre="Mouse", precio=50000, stock=20),
    Producto(nombre="Monitor", precio=800000, stock=5),
]

db.add_all(productos)
db.commit()
db.close()

print("How do you turn this on?")