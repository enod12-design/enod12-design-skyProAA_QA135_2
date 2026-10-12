def __init__(self, page: Page) -> None:
    self.page: Page = page
    # Локатор строки поиска на Кинопоиске
    self.search_input = page.locator("input[name='kp_query']")
    # Локатор кнопки поиска или формы
    self.search_button = page.locator("button[type='submit'], [data-tid='63b05890']")
    # Локатор логотипа
    self.logo = page.locator("a[href='/'], [aria-label='Кинопоиск']")
    # Онлайн-кинотеатр ссылка
    self.online_cinema_link = page.locator("a:has-text('Онлайн-кинотеатр')")


def open(self, url: str) -> None:
    self.page.goto(url, wait_until="domcontentloaded")


def search_movie(self, title: str) -> None:
    self.search_input.click()
    self.search_input.fill(title)
    self.search_input.press("Enter")

