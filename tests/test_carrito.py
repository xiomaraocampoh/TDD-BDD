import pytest
from src.carrito.carrito import Carrito
from src.carrito.modelos import Producto

def test_agregar_producto_nuevo(): #necesario para eliminar depues
    carrito = Carrito()
    producto = Producto(nombre="laptop", precio_unitario=1500.0, cantidad=1)
    
    carrito.agregar(producto)
    
    assert "laptop" in carrito.items
    assert carrito.items["laptop"].cantidad == 1

def test_eliminar_producto():
    #Rf, 2
    carrito = Carrito()
    producto = Producto(nombre="mouse", precio_unitario=25.0, cantidad=2)
    carrito.agregar(producto)
    
    carrito.eliminar("mouse")
    
    assert "mouse" not in carrito.items

def test_calcular_total_carrito():
    #Rf, 3
    carrito = Carrito()
    carrito.agregar(Producto(nombre="mouse", precio_unitario=25.0, cantidad=2))   # Subtotal: 50.0
    carrito.agregar(Producto(nombre="teclado", precio_unitario=50.0, cantidad=1)) # Subtotal: 50.0
    
    total = carrito.calcular_total()
    
    assert total == 100.0

def test_vaciar_carrito():
    carrito = Carrito()
    carrito.agregar(Producto(nombre="laptop", precio_unitario=1500.0, cantidad=1))
    carrito.agregar(Producto(nombre="mouse", precio_unitario=25.0, cantidad=1))
    
    carrito.vaciar()
  
    assert len(carrito.items) == 0