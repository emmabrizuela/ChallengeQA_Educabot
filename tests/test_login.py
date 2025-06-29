import pytest
from pages.login_page import LoginPage

def test_login_exitoso(driver):
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url

def test_login_usuario_bloqueado(driver):
    login = LoginPage(driver)
    login.login("locked_out_user", "secret_sauce")
    assert "locked out" in login.get_error_message().lower()

def test_login_campos_vacios(driver):
    login = LoginPage(driver)
    login.login("", "")
    assert "required" in login.get_error_message().lower()
