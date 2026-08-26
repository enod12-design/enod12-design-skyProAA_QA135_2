from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    url = "https://httpbin.qa-territory.online/forms/post"
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")

    input_field = driver.find_element(By.NAME, "custname")
    input_field.send_keys("Алексей")

    submit_button = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Submit')]"
    )
    submit_button.click()

    assert driver.current_url != url

    driver.quit()
