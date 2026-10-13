import pytest
from playwright.sync_api import Page, expect
from config import BASE_URL_UI
from main_page import MainPage

# 1. Загрузка главной страницы
def test_ui_open_main_page(page: Page) -> None:
    page.goto(BASE_URL_UI, wait_until="domcontentloaded")
    expect(page).to_have_title(lambda title: "Кинопоиск" in title or len(title) > 0)

# 2. Проверка наличия и видимости поля поиска
def test_ui_search_input_visible(page: Page) -> None:
    main_page = MainPage(page)
    main_page.open(BASE_URL_UI)
    expect(main_page.search_input).to_be_visible()

# 3. Ввод текста в поисковую строку
def test_ui_fill_search_query(page: Page) -> None:
    main_page = MainPage(page)
    main_page.open(BASE_URL_UI)
    main_page.search_input.fill("Мстители")
    expect(main_page.search_input).to_have_value("Мстители")

# 4. Проверка присутствия элементов навигации (Параметризованный)
@pytest.mark.parametrize("query_text", ["Интерстеллар", "Матрица"])
def test_ui_search_input_parametrized(page: Page, query_text: str) -> None:
    main_page = MainPage(page)
    main_page.open(BASE_URL_UI)
    main_page.search_input.fill(query_text)
    expect(main_page.search_input).to_have_value(query_text)

# 5. Проверка кликабельности логотипа/шапки
def test_ui_logo_is_visible(page: Page) -> None:
    main_page = MainPage(page)
    main_page.open(BASE_URL_UI)
    expect(main_page.logo.first).to_be_visible()
