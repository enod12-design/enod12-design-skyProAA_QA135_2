import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    """Класс для работы со страницей авторизации."""

    def __init__(self, driver: WebDriver) -> None:
        """Инициализация элементов страницы."""
        self.driver = driver
        self.url: str = "https://www.saucedemo.com/"
        self._username = (By.ID, "user-name")
        self._password = (By.ID, "password")
        self._login_btn = (By.ID, "login-button")

    @allure.step("Открытие страницы авторизации")
    def open(self) -> None:
        """Открывает главную страницу авторизации."""
        self.driver.get(self.url)

    @allure.step("Выполнение входа с логином: {username}")
    def login(self, username: str, password: str) -> None:
        """
        Заполняет форму авторизации и нажимает кнопку входа.

        :param username: Логин пользователя
        :param password: Пароль пользователя
        """
        wait = WebDriverWait(self.driver, timeout=10)

        # Ждем появление первого поля ввода
        first_input = wait.until(
            EC.visibility_of_element_located(self._username)
        )
        first_input.send_keys(username)

        self.driver.find_element(*self._password).send_keys(password)
        self.driver.find_element(*self._login_btn).click()
