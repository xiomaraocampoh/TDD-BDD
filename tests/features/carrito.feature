# tests/features/carrito.feature

Feature: Gestión del carrito de compras
  Como cliente de la tienda
  Quiero poder gestionar los productos de mi carrito
  Para saber exactamente qué voy a comprar y cuánto voy a pagar

  Scenario: Eliminar un producto del carrito 
    Given que tengo un carrito con 2 "mouse" a 25.0 cada uno
    When elimino el producto "mouse"
    Then el carrito no debe contener "mouse"

  Scenario: Calcular el total del carrito 
    Given que tengo un carrito vacío
    And agrego 2 "mouse" a 25.0 cada uno
    And agrego 1 "teclado" a 50.0 cada uno
    When calculo el total
    Then el total a pagar debe ser 100.0