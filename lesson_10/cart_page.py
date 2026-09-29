import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CartPage:
    """Класс для работы со страницей корзины."""

    def __init__(self, driver: WebDriver) -> None:
        """Инициализация элементов страницы."""
        self.driver = driver
        self._checkout_btn = (By.ID, "checkout")

    @allure.step("Нажатие кнопки перехода к оформлению заказа (Checkout)")
    def click_checkout(self) -> None:
        """Переходит на страницу оформления заказа."""
        wait = WebDriverWait(self.driver, timeout=10)
        checkout_element = wait.until(
            EC.element_to_be_clickable(self._checkout_btn)
        )
        checkout_element.click()
