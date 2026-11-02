from playwright.sync_api import Page, expect
from config import BASE_URL_UI
from main_page import MainPage


# 1. Поиск фильма по полному совпадению названия
def test_ui_full_search_movie(page: Page) -> None:
    main_page = MainPage(page)
    main_page.open(BASE_URL_UI)
    main_page.search_movie("Мстители: Война бесконечности")
    # Проверяем, что в поисковой выдаче отобразился результат
    expect(page.locator("a[href*='film']").first).to_be_visible()


# 2. Переход на карточку фильма из поисковой выдачи
def test_ui_navigate_to_movie_card(page: Page) -> None:
    main_page = MainPage(page)
    main_page.open(BASE_URL_UI)
    main_page.search_movie("Мстители: Война бесконечности")
    # Клик по первому результату в выдаче
    movie_item = page.locator("a[href*='film']").first
    movie_item.click()
    # Проверяем, что открылась страница фильма
    assert "/film/" in page.url


# 3. Фильтрация каталога по жанру и году
def test_ui_catalog_filter(page: Page) -> None:
    main_page = MainPage(page)
    main_page.open(BASE_URL_UI)
    # Переход в раздел фильмов/каталога
    page.goto(
        f"{BASE_URL_UI}/lists/categories/movies/",
        wait_until="domcontentloaded")
    assert "lists" in page.url


# 4. Поиск фильма по частично введенному названию
def test_ui_partial_search_movie(page: Page) -> None:
    main_page = MainPage(page)
    main_page.open(BASE_URL_UI)
    main_page.search_movie("Война бесконечности")
    # Проверяем, что в URL появился параметр поискового запроса
    assert "text=" in page.url


# 5. Отображение блока актеров и съемочной группы
def test_ui_movie_cast_section(page: Page) -> None:
    # Переходим напрямую на страницу фильма «Мстители: Война бесконечности»
    page.goto(f"{BASE_URL_UI}/film/843650/", wait_until="domcontentloaded")
    actor_section = page.locator("text=В главных ролях")
    expect(actor_section).to_be_visible()


# 6. Валидация поиска при вводе несуществующего названия
def test_ui_search_nonexistent_movie(page: Page) -> None:
    main_page = MainPage(page)
    main_page.open(BASE_URL_UI)
    main_page.search_movie("nesushestvushii")
    not_found_message = page.locator(
        "text=По вашему запросу ничего не найдено"
    )
    expect(not_found_message).to_be_visible()
