from dataclasses import dataclass

@dataclass
class Producto:
    nombre: str
    precio_unitario: float
    cantidad: int