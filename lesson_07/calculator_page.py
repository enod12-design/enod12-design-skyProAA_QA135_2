from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = (
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )

        self._delay_input = (By.CSS_SELECTOR, "#delay")
        self._screen = (By.CLASS_NAME, "screen")

    def open(self):
        self.driver.get(self.url)

    def set_delay(self, seconds: str):
        delay_element = self.driver.find_element(*self._delay_input)
        delay_element.clear()
        delay_element.send_keys(seconds)

    def click_button(self, button_text: str):
        button_locator = (By.XPATH, f"//span[text()='{button_text}']")
        button = self.driver.find_element(*button_locator)
        self.driver.execute_script("arguments[0].click();", button)

    def get_result_with_wait(
            self, expected_text: str, timeout: int = 50) -> str:
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self._screen, expected_text)
        )
        return self.driver.find_element(*self._screen).text
