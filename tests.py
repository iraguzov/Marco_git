from playwright.sync_api import sync_playwright

def test_check_page_title():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # headless=False to open the browser visibly
        page = browser.new_page()
        page.goto("https://neuralms.com")
        assert page.title() == "Neural MS Consulting - "
        browser.close()


test_check_page_title()