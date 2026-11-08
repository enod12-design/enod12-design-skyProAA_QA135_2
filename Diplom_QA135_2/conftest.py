from typing import Generator
import pytest
from playwright.sync_api import Page, sync_playwright
from config import API_KEY


@pytest.fixture(scope="session")
def api_headers() -> dict[str, str]:
    return {
        "X-API-KEY": API_KEY,
        "Content-Type": "application/json"
    }


@pytest.fixture(scope="function")
def page() -> Generator[Page, None, None]:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()
