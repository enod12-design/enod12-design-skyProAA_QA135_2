import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@pytest.fixture
def driver():
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(
        service=Service(GeckoDriverManager().install()), options=options
    )
    driver.implicitly_wait(10)

    yield driver

    driver.quit()


def test_store_checkout_total(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open()

    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.add_to_cart("Sauce Labs Bolt T-Shirt")
    inventory_page.add_to_cart("Sauce Labs Onesie")

    inventory_page.go_to_cart()

    cart_page.click_checkout()

    checkout_page.fill_form(
        first_name="Алексей",
        last_name="Афанасьев",
        postal_code="125211"
    )

    actual_total = checkout_page.get_total_price()

    assert "Total: $58.29" in actual_total
