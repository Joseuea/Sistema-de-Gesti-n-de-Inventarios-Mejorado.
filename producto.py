from dataclasses import dataclass

@dataclass
class Producto:
    id: str
    nombre: str
    precio: float
    cantidad: int
