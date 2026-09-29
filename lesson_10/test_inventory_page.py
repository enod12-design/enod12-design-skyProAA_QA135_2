import allure
import pytest
from login_page import LoginPage
from inventory_page import InventoryPage


@allure.feature("Каталог товаров")
@allure.story("Взаимодействие с товарами")
class TestInventoryPage:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Предусловие: авторизация перед каждым тестом."""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

    @allure.title("Добавление товара в корзину")
    @allure.description(
        "Проверка добавления товара по его названию со страницы каталога."
    )
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_item_to_cart(self, driver):
        inventory_page = InventoryPage(driver)

        inventory_page.add_to_cart("Sauce Labs Backpack")

        with allure.step("Проверка: счетчик корзины обновился"):
            # Проверка отображения количества товаров в значке корзины
            badge = driver.find_element("class name", "shopping_cart_badge")
            assert badge.text == "1"

    @allure.title("Переход из каталога в корзину")
    @allure.description("Проверка кликабельности кнопки перехода в корзину.")
    @allure.severity(allure.severity_level.NORMAL)
    def test_go_to_cart(self, driver):
        inventory_page = InventoryPage(driver)

        inventory_page.go_to_cart()

        with allure.step("Проверка: открыта страница корзины"):
            assert "cart.html" in driver.current_url
