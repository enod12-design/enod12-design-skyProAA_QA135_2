import allure
from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage


@allure.feature("Корзина")
@allure.story("Переход к оформлению")
class TestCartPage:

    @allure.title("Переход из корзины к оформлению заказа (Checkout)")
    @allure.description(
        "Тест проверяет нажатие кнопки Checkout в корзине покупок."
    )
    @allure.severity(
        allure.severity_level.CRITICAL
    )
    def test_proceed_to_checkout(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)

        # Подготовка: логин и переход в корзину
        login_page.open()
        login_page.login("standard_user", "secret_sauce")
        inventory_page.add_to_cart("Sauce Labs Backpack")
        inventory_page.go_to_cart()

        # Тестируемое действие
        cart_page.click_checkout()

        with allure.step("Проверка: открыт первый шаг оформления заказа"):
            assert "checkout-step-one.html" in driver.current_url
