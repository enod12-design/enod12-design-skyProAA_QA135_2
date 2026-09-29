import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """Класс для работы со страницей оформления заказа."""

    def __init__(self, driver: WebDriver) -> None:
        """Инициализация элементов страницы.
        :param driver: экземпляр WebDriver
        """
        self.driver = driver
        self._first_name = (By.ID, "first-name")
        self._last_name = (By.ID, "last-name")
        self._postal_code = (By.ID, "postal-code")
        self._continue_btn = (By.ID, "continue")
        self._total_label = (By.CLASS_NAME, "summary_total_label")

    @allure.step(
        "Заполнение формы оформления заказа: {first_name} {last_name}, "
        "{postal_code}"
    )
    def fill_form(
            self, first_name: str, last_name: str, postal_code: str
    ) -> None:
        """Заполняет форму персональными данными
        и нажимает кнопку продолжения.
        :param first_name: имя покупателя
        :param last_name: фамилия покупателя
        :param postal_code: почтовый индекс
        """
        wait = WebDriverWait(self.driver, 10)

        # Ждем появление первoго поля
        first_input = wait.until(
            EC.visibility_of_element_located(self._first_name)
        )
        first_input.send_keys(first_name)

        self.driver.find_element(*self._last_name).send_keys(last_name)
        self.driver.find_element(*self._postal_code).send_keys(postal_code)
        self.driver.find_element(*self._continue_btn).click()

    @allure.step("Получение итоговой стоимости заказа")
    def get_total_price(self) -> str:
        """Возвращает итоговую стоимость заказа.
        :return: итоговая стоимость заказа
        :rtype: str
        """
        wait = WebDriverWait(self.driver, 10)
        total_element = wait.until(
            EC.visibility_of_element_located(self._total_label)
        )
        return total_element.text
