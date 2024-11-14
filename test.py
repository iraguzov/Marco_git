from playwright.sync_api import sync_playwright

def check_page_title():
    with sync_playwright() as p:
        # Launch a browser (Chrome in this case)
        browser = p.chromium.launch(headless=False)  # headless=False to open the browser visibly
        page = browser.new_page()
        # Go to the specified URL
        page.goto("https://neuralms.com")
        # Check the title of the page
        expected_title = "Neural MS Consulting - Home"
        actual_title = page.title()
        # Print result based on title match
        if actual_title == expected_title:
            print("pass")
        else:
            print("fail")
        # Close the browser
        browser.close()

check_page_title()