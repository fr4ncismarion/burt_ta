import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="module")
def browser_setup():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto("https://testpages.eviltester.com/styled/calculator")
        yield page
        browser.close()
