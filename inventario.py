from producto import Producto
from excepciones import ProductoNoEncontradoError, ProductoDuplicadoError

class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, p: Producto):
        if p.id in self.productos:
            raise ProductoDuplicadoError(f"Ya existe un producto con id {p.id}")
        self.productos[p.id] = p

    def obtener_producto(self, pid: str) -> Producto:
        if pid not in self.productos:
            raise ProductoNoEncontradoError(f"No existe producto con id {pid}")
        return self.productos[pid]

    def listar_productos(self):
        return list(self.productos.values())

    def eliminar_producto(self, pid: str):
        if pid not in self.productos:
            raise ProductoNoEncontradoError(f"No existe producto con id {pid}")
        del self.productos[pid]

    def actualizar_cantidad(self, pid: str, nueva_cantidad: int):
        if pid not in self.productos:
            raise ProductoNoEncontradoError(f"No existe producto con id {pid}")
        self.productos[pid].cantidad = nueva_cantidad

    def actualizar_precio(self, pid: str, nuevo_precio: float):
        if pid not in self.productos:
            raise ProductoNoEncontradoError(f"No existe producto con id {pid}")
        self.productos[pid].precio = nuevo_precio
