from playwright.sync_api import Page


class MainPage:
    def __init__(self, page: Page) -> None:
        self.page: Page = page
        # Универсальные селекторы для поиска поля ввода на Кинопоиске
        self.search_input = page.locator(
            "input[name='text'], input[name='kp_query'], input[type='text']"
        ).first
        # Локатор логотипа
        self.logo = page.locator("a[href='/'], [aria-label='Кинопоиск']").first

    def open(self, url: str) -> None:
        self.page.goto(url, wait_until="domcontentloaded")

    def search_movie(self, title: str) -> None:
        self.search_input.click()
        self.search_input.fill(title)
        self.search_input.press("Enter")
