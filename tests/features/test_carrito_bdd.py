# tests/test_carrito_bdd.py
import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from src.carrito.carrito import Carrito
from src.carrito.modelos import Producto

scenarios('carrito.feature')

@pytest.fixture
def carrito():
    return Carrito()


@given(parsers.parse('que tengo un carrito con {cantidad} "{nombre}" a {precio} cada uno'))
def carrito_con_producto(carrito, cantidad, nombre, precio):
    producto = Producto(nombre=nombre, precio_unitario=float(precio), cantidad=int(cantidad))
    carrito.agregar(producto)

@when(parsers.parse('elimino el producto "{nombre}"'))
def eliminar_producto(carrito, nombre):
    carrito.eliminar(nombre)

@then(parsers.parse('el carrito no debe contener "{nombre}"'))
def verificar_eliminacion(carrito, nombre):
    assert nombre not in carrito.items

@given('que tengo un carrito vacío')
def carrito_vacio(carrito):
    carrito.items.clear()

@given(('agrego {cantidad} "{nombre}" a {precio} cada uno'))
def agregar_producto(carrito, cantidad, nombre, precio):
    producto = Producto(nombre=nombre, precio_unitario=float(precio), cantidad=int(cantidad))
    carrito.agregar(producto)

@when('calculo el total', target_fixture='total_calculado')
def calculo_total(carrito):
    return carrito.calcular_total()

@then(parsers.parse('el total a pagar debe ser {total_esperado}'))
def verificar_total(total_calculado, total_esperado):
    assert total_calculado == float(total_esperado)
