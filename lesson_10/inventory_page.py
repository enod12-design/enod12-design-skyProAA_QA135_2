import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class InventoryPage:
    """Класс для работы с главной страницей каталога товаров."""

    def __init__(self, driver: WebDriver) -> None:
        """Инициализация элементов страницы.
        :param driver: экземпляр WebDriver
        """
        self.driver = driver
        self._cart_link = (By.CLASS_NAME, "shopping_cart_link")

    @allure.step("Добавление товара '{item_name}' в корзину")
    def add_to_cart(self, item_name: str) -> None:
        """
        Добавляет указанный товар в корзину по его названию.

        :param item_name: Название товара (например, 'Sauce Labs Backpack')
        """
        wait = WebDriverWait(self.driver, timeout=10)
        button_id = f"add-to-cart-{item_name.lower().replace(' ', '-')}"

        button_element = wait.until(
            EC.element_to_be_clickable((By.ID, button_id))
        )
        button_element.click()

    @allure.step("Переход в корзину покупок")
    def go_to_cart(self) -> None:
        """Переходит на страницу корзины."""
        wait = WebDriverWait(self.driver, timeout=10)
        cart_element = wait.until(
            EC.element_to_be_clickable(self._cart_link)
        )
        cart_element.click()
