import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from checkout_page import CheckoutPage


@allure.title("Проверка успешного оформления заказа")
@allure.description(
    "Тест проверяет корректность расчета итоговой стоимости после заполнения"
    " формы данных."
)
@allure.feature("Оформление заказа")
@allure.severity(allure.severity_level.CRITICAL)
def test_checkout_total_price(driver):
    wait = WebDriverWait(driver, 10)

    # 1. Переходим на сайт и авторизуемся
    driver.get("https://www.saucedemo.com/")

    wait.until(
        EC.element_to_be_clickable((By.ID, "user-name"))
    ).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # 2. Добавляем товар и переходим в корзину / чекаут с ожиданиями
    wait.until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
    ).click()

    wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
    ).click()

    wait.until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    ).click()

    # 3. Выполняем шаги Page Object
    checkout_page = CheckoutPage(driver)

    with allure.step("Заполнение персональных данных"):
        checkout_page.fill_form(
            first_name="Алексей", last_name="Афанасьев", postal_code="155232"
        )

    with allure.step("Проверка: Итоговая сумма соответствует ожидаемой"):
        total_price = checkout_page.get_total_price()
        assert total_price == "Total: $32.39"
