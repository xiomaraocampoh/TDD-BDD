import time

from src.carrito.carrito import Carrito
from src.carrito.modelos import Producto


def generar_productos(cantidad: int):
    return [Producto(nombre=f"producto_{i}", precio_unitario=1.0 + i * 0.01, cantidad=1) for i in range(cantidad)]


def test_agregar_muchos_productos_rendimiento():
    carrito = Carrito()
    productos = generar_productos(10000)

    inicio = time.perf_counter()
    for producto in productos:
        carrito.agregar(producto)
    duracion = time.perf_counter() - inicio

    assert len(carrito.items) == 10000
    assert duracion < 0.5, f"La operación de agregar {len(productos)} productos tardó demasiado: {duracion:.3f}s"


def test_calcular_total_gran_carrito_rendimiento():
    carrito = Carrito()
    productos = generar_productos(20000)
    for producto in productos:
        carrito.agregar(producto)

    inicio = time.perf_counter()
    total = carrito.calcular_total()
    duracion = time.perf_counter() - inicio

    assert total > 0
    assert duracion < 0.2, f"El cálculo del total de {len(carrito.items)} productos tardó demasiado: {duracion:.3f}s"
