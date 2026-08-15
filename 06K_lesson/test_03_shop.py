from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop_checkout():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 10)

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    wait.until(
        EC.element_to_be_clickable(
            (By.ID, "add-to-cart-sauce-labs-backpack")
        )
    ).click()
    wait.until(
        EC.element_to_be_clickable(
            (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        )
    ).click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    wait.until(
        EC.element_to_be_clickable((By.ID, "checkout"))).click()

    wait.until(
        EC.presence_of_element_located((By.ID, "first-name"))
    ).send_keys("Алексей")
    driver.find_element(By.ID, "last-name").send_keys("Афанасьев")
    driver.find_element(By.ID, "postal-code").send_keys("125222")

    driver.find_element(By.ID, "continue").click()

    total_element = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )
    total_text = total_element.text

    assert "58.29" in total_text

    driver.quit()
