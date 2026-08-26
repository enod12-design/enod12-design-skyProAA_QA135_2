from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self._checkout_btn = (By.ID, "checkout")

    def click_checkout(self):
        self.driver.find_element(*self._checkout_btn).click()
