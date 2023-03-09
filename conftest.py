import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def page4():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
