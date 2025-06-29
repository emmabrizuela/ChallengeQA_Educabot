import pytest
from pages.login_page import LoginPage
from pages.inventario_page import InventarioPage
from pages.carrito_page import CarritoPage

def login_y_ir_a_inventario(driver):
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")
    return InventarioPage(driver)

def test_agregar_al_carrito(driver):
    inventario = login_y_ir_a_inventario(driver)
    inventario.add_product()
    inventario.go_to_cart()
    carrito = CarritoPage(driver)
    assert carrito.is_item_present()

def test_remover_producto(driver):
    inventario = login_y_ir_a_inventario(driver)
    inventario.add_product()
    inventario.remove_product()
    inventario.go_to_cart()
    carrito = CarritoPage(driver)
    assert not carrito.is_item_present()

def test_checkout(driver):
    inventario = login_y_ir_a_inventario(driver)
    inventario.add_product()
    inventario.go_to_cart()
    carrito = CarritoPage(driver)
    carrito.checkout()
    assert "checkout-step-one" in driver.current_url
