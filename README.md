# Sistema de Facturación API

API REST desarrollada con **FastAPI** para la gestión de clientes, productos, ventas y facturas.

## Descripción

Este proyecto implementa un sistema básico de facturación que permite:

* Registrar clientes.
* Registrar productos.
* Realizar compras.
* Generar facturas automáticamente.
* Consultar las facturas de un cliente.
* Gestionar el stock de los productos.

El proyecto fue desarrollado con fines académicos para practicar el desarrollo de APIs REST utilizando Python y FastAPI, futuramente puede ser publicado como recurso abierto.

---

## Tecnologías utilizadas

* Python 3.x
* FastAPI
* Uvicorn
* Pydantic
* PostgreSQL 
* Git y GitHub

---

## Estructura del proyecto

Esto fue lo primero que se definio antes de comenzar a desarrollar, cabe destacar que fue elaborado primero a mano y en papel y lapiz.

```plaintext
facturas/
│
├── endpoints/
│   └── main.py
│
├── models/
│   ├── cliente.py
│   ├── producto.py
│   ├── venta.py
│   └── factura.py
│
├── requirements.txt
└── README.md
```

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd facturas
```

### 2. Crear un entorno virtual

```bash
uv venv
```

### 3. Activar el entorno virtual

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux/Mac

```bash
source .venv/bin/activate
```

### 4. Instalar las dependencias

```bash
uv pip install -r requirements.txt
```

---

## Ejecutar el proyecto

```bash
uvicorn endpoints.main:app --reload
```

La documentación de la API estará disponible en:

* Swagger UI: http://127.0.0.1:8000/docs
* ReDoc: http://127.0.0.1:8000/redoc

---

## Endpoints disponibles

### Clientes

| Método | Ruta            | Descripción               |
| ------ | --------------- | ------------------------- |
| POST   | `/usuarioCrear` | Crear un cliente          |
| GET    | `/usuarios`     | Listar todos los clientes |

### Productos

| Método | Ruta             | Descripción          |
| ------ | ---------------- | -------------------- |
| POST   | `/productoCrear` | Crear un producto    |
| GET    | `/productos`     | Listar los productos |

### Ventas

| Método | Ruta     | Descripción                               |
| ------ | -------- | ----------------------------------------- |
| POST   | `/venta` | Realizar una compra y generar una factura |

### Facturas

| Método | Ruta                     | Descripción                        |
| ------ | ------------------------ | ---------------------------------- |
| GET    | `/facturas/{cliente_id}` | Obtener las facturas de un cliente |

---

## Ejemplo de compra

```json
{
  "cliente_id": 1,
  "producto_id": 2,
  "cantidad": 3
}
```

---

## Flujo de funcionamiento

Este flujo fue primero escrito a mano y luego pasado a README.

1. Crear un cliente.
2. Crear uno o varios productos.
3. Realizar una compra.
4. Verificar la disminución del stock.
5. Consultar la factura generada.

---

## Funcionalidades implementadas

* [x] Gestión de clientes
* [x] Gestión de productos
* [x] Registro de ventas
* [x] Generación de facturas
* [x] Consulta de facturas por cliente
* [x] Descuento automático del stock

---

## Autor

**Luis Camilo**

Proyecto desarrollado con fines académicos.
