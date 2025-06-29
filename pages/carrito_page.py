from selenium.webdriver.common.by import By

class CarritoPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")
        self.cart_item = (By.CLASS_NAME, "cart_item")

    def is_item_present(self):
        return len(self.driver.find_elements(*self.cart_item)) > 0

    def checkout(self):
        self.driver.find_element(*self.checkout_button).click()
