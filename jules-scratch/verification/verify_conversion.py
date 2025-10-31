import os
from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()

    # Get the absolute path to the index.html file
    file_path = os.path.abspath('index.html')

    page.goto(f'file://{file_path}')

    # Upload the dummy FLAC file
    page.set_input_files('input#fileInput', 'test.flac')

    page.click('button#convertButton')

    # Wait for the download link to appear
    page.wait_for_selector('ul#convertedFiles li a')

    page.screenshot(path='jules-scratch/verification/verification.png')

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
