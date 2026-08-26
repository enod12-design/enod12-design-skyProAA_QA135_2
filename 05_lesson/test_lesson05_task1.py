from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    start_url = "https://httpbin.qa-territory.online"
    driver = webdriver.Chrome()
    driver.get(start_url)
    html_form_link = driver.find_element(
        By.XPATH, "//a[contains(text(), 'HTML Form')]"
    )
    html_form_link.click()

    assert "/forms/post" in driver.current_url

    driver.back()
    driver.quit()
