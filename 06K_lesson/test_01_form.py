# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_fill_form(driver):
    url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    driver.get(url)

    wait = WebDriverWait(driver, 10)

    wait.until(
        EC.presence_of_element_located((By.NAME, "first-name"))
    ).send_keys("Алексей")
    driver.find_element(By.NAME, "last-name").send_keys("Афанасьев")
    driver.find_element(By.NAME, "address").send_keys("Калатушкина, 13-5")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+79254443322")

    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    submit_button = driver.find_element(
        By.CSS_SELECTOR, "button[type='submit']")
    driver.execute_script("arguments[0].click();", submit_button)

    wait.until(EC.presence_of_element_located((By.ID, "zip-code")))

    zip_code = driver.find_element(By.ID, "zip-code")
    assert "alert-danger" in zip_code.get_attribute("class")

    green_fields_ids = [
        "first-name",
        "last-name",
        "address",
        "e-mail",
        "phone",
        "city",
        "country",
        "job-position",
        "company"
    ]

    for field_id in green_fields_ids:
        field_element = driver.find_element(By.ID, field_id)
        field_classes = field_element.get_attribute("class")
        assert "alert-success" in field_classes, (
            f"Поле {field_id} должно быть подсвечено зеленым!"
        )
