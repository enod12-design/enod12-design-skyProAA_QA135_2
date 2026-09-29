import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    # Инициализация браузера Chrome
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)  # Неявное ожидание
    browser.maximize_window()

    yield browser  # Передает объект браузера в тест

    # Завершение работы после прохождения теста
    browser.quit()
