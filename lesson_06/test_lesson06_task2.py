from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()

    cookie_user1 = {
        'name': 'usertest12345',
        'value': 'NjliYmFkNGMtZGFiOS00NGFhLWIzY2YtODUxOTBmYTIyMTVk'
    }
    cookie_user2 = {
        'name': 'usertest678910',
        'value': 'M2ZhZWY1ZWUtYWM0ZS00MjA3LWJhN2ItZjdiODg2YWI4NDJm'
    }

    user1_profile_url = 'https://gitflic.ru/user/usertest12345'
    user2_profile_url = 'https://gitflic.ru/user/usertest678910'

    # 1. Откройте страницу http://gitflic.ru
    driver.get('http://gitflic.ru')

    # 2. Установите cookie пользователя 1
    driver.add_cookie(cookie_user1)

    # 3. Обновите страницу
    driver.refresh()

    # 4. Перейдите на страницу пользователя
    driver.get(user1_profile_url)

    # 5. Сохраните текущий URL.
    url_user1 = driver.current_url

    # 6. Разлогиньтесь(очистите куки).
    driver.delete_all_cookies()

    # 7. Установите cookie пользователя 2.
    driver.get('http://gitflic.ru/')
    driver.add_cookie(cookie_user2)

    # 8. Обновите страницу.
    driver.refresh()

    # 9. Перейдите на страницу пользователя 2.
    driver.get(user2_profile_url)

    # 10. Сохраните текущий URL.
    url_user2 = driver.current_url

    # 11. Проверьте, что URL для пользователя 1 и пользователя 2 различаются.
    assert url_user1 != url_user2, (
        f'URL совпадают, хотя должны различаться: {url_user1}'
    )

    driver.quit()
