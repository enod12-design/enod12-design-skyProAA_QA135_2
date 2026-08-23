from selenium.webdriver.common.by import By


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self._cart_link = (By.CLASS_NAME, "shopping_cart_link")

    def add_to_cart(self, item_name: str):
        button_id = f"add-to-cart-{item_name.lower().replace(' ', '-')}"
        self.driver.find_element(By.ID, button_id).click()

    def go_to_cart(self):
        self.driver.find_element(*self._cart_link).click()
