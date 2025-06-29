from selenium.webdriver.common.by import By

class InventarioPage:
    def __init__(self, driver):
        self.driver = driver
        self.title = (By.CLASS_NAME, "title")
        self.add_backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.remove_backpack = (By.ID, "remove-sauce-labs-backpack")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def add_product(self):
        self.driver.find_element(*self.add_backpack).click()

    def remove_product(self):
        self.driver.find_element(*self.remove_backpack).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_icon).click()

    def get_title(self):
        return self.driver.find_element(*self.title).text
