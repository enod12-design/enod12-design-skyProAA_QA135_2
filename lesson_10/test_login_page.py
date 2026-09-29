import allure
from login_page import LoginPage


@allure.feature("Авторизация")
@allure.story("Форма входа в систему")
class TestLoginPage:

    @allure.title("Успешная авторизация с валидными данными")
    @allure.description("Тест проверяет вход"
                        " в систему под стандартным пользователем.")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_successful_login(self, driver):
        login_page = LoginPage(driver)

        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        with allure.step("Проверка: успешный переход в каталог товаров"):
            assert "inventory.html" in driver.current_url

    @allure.title("Авторизация заблокированного пользователя")
    @allure.description(
        "Тест проверяет обработку ошибки "
        "при попытке входа заблокированного пользователя."
    )
    @allure.severity(allure.severity_level.CRITICAL)
    def test_locked_out_user_login(self, driver):
        login_page = LoginPage(driver)

        login_page.open()
        login_page.login("locked_out_user", "secret_sauce")

        with allure.step("Проверка: остаемся на странице логина"):
            assert "inventory.html" not in driver.current_url
