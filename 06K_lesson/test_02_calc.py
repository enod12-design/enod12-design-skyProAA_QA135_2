from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_slow_calculator():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 50)

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )

    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")

    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()

    wait.until(EC.invisibility_of_element_located(
        (By.CSS_SELECTOR, "#spinner"))
    )
    btn_equal = driver.find_element(By.XPATH, "//span[text()='=']")
    driver.execute_script("arguments[0].click();", btn_equal)

    wait.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
    )

    result_text = driver.find_element(By.CSS_SELECTOR, ".screen").text
    assert result_text == "15"

    driver.quit()
