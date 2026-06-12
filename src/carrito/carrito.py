from typing import Dict
from src.carrito.modelos import Producto

class Carrito:
    def __init__(self):
        self.items: Dict[str, Producto] = {}

    def agregar(self, producto: Producto):
        if producto.nombre in self.items:
            self.items[producto.nombre].cantidad += producto.cantidad
        else:
            self.items[producto.nombre] = producto

    def eliminar(self, nombre_producto: str):
        if nombre_producto in self.items:
            del self.items[nombre_producto]

    def calcular_total(self) -> float:
        total = sum(item.precio_unitario * item.cantidad for item in self.items.values())
        return total
    
    def vaciar(self):
        self.items.clear()