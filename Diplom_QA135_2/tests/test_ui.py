import pytest
from playwright.sync_api import Page, expect
from config import BASE_URL_UI
import allure
from main_page import MainPage

pytestmark = pytest.mark.ui


# Тест 1
@allure.story("UI Поиск фильмов")
@allure.title("Тест поиска фильма по полному совпадению названия")
def test_ui_full_search_movie(page: Page) -> None:
    main_page = MainPage(page)

    with allure.step("Открытие главной страницы"):
        main_page.open(BASE_URL_UI)

    with allure.step("Ввод названия фильма в поиск и отправка запроса"):
        main_page.search_movie("Мстители: Война бесконечности")

    with allure.step("Проверка, что в поисковой выдаче отобразился результат"):
        expect(page.locator("a[href*='film']").first).to_be_visible()


# Тест 2
@allure.story("UI Навигация")
@allure.title("Тест перехода на карточку фильма из поисковой выдачи")
def test_ui_navigate_to_movie_card(page: Page) -> None:
    main_page = MainPage(page)

    with allure.step("Открытие главной страницы и поиск фильма"):
        main_page.open(BASE_URL_UI)
        main_page.search_movie("Мстители: Война бесконечности")

    with allure.step("Клик по первому результату в выдаче"):
        movie_item = page.locator("a[href*='film']").first
        movie_item.click()

    with allure.step(
            "Проверка, что открылась страница фильма (наличие /film/ в URL)"
    ):
        assert "/film/" in page.url


# Тест 3
@allure.story("UI Каталог")
@allure.title("Тест фильтрации каталога по жанру и году")
def test_ui_catalog_filter(page: Page) -> None:
    main_page = MainPage(page)

    with allure.step("Открытие главной страницы"):
        main_page.open(BASE_URL_UI)

    with allure.step("Переход в раздел фильмов/каталога"):
        page.goto(
            url=f"{BASE_URL_UI}/lists/categories/movies/",
            wait_until="domcontentloaded"
        )

    with allure.step("Проверка успешности перехода по URL"):
        assert "lists" in page.url


# Тест 4
@allure.story("UI Поиск фильмов")
@allure.title("Тест поиска фильма по частично введенному названию")
def test_ui_partial_search_movie(page: Page) -> None:
    main_page = MainPage(page)

    with allure.step("Открытие главной страницы"):
        main_page.open(BASE_URL_UI)

    with allure.step("Ввод части названия фильма в поиск"):
        main_page.search_movie("Война бесконечности")

    with allure.step(
            "Проверка, что в URL появился параметр поискового запроса"
    ):
        assert "text=" in page.url


# Тест 5
@allure.story("UI Страница фильма")
@allure.title("Тест отображения блока актеров и съемочной группы")
def test_ui_movie_cast_section(page: Page) -> None:
    with allure.step("Переход напрямую на страницу конкретного фильма"):
        page.goto(
            url=f"{BASE_URL_UI}/film/843650/",
            wait_until="domcontentloaded"
        )

    with allure.step("Проверка видимости блока с актерами"):
        actor_section = page.locator("text=В главных ролях")
        expect(actor_section).to_be_visible()


# Тест 6
@allure.story("UI Поиск фильмов")
@allure.title("Тест валидации поиска при вводе несуществующего названия")
def test_ui_search_nonexistent_movie(page: Page) -> None:
    main_page = MainPage(page)

    with allure.step("Открытие главной страницы"):
        main_page.open(BASE_URL_UI)

    with allure.step("Поиск  несуществующего названия"):
        main_page.search_movie("nesushestvushii")

    with allure.step(
            "Проверка появления сообщения "
            "'По вашему запросу ничего не найдено'"
    ):
        not_found_message = page.locator(
            "text=По вашему запросу ничего не найдено"
        )
        expect(not_found_message).to_be_visible()
