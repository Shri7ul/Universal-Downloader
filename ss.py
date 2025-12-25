from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(
        viewport={"width": 1400, "height": 900}
    )
    page.goto("http://localhost:8501", wait_until="networkidle")

    # wait a bit for Streamlit to fully render
    page.wait_for_timeout(2000)

    page.screenshot(
        path="proof.png",
        full_page=True
    )

    browser.close()
