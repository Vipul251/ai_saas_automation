
from playwright.sync_api import sync_playwright
import os
from bs4 import BeautifulSoup
import pandas as pd
import time
from dotenv import load_dotenv
load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

def login_and_scrape_users():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        try:
            print("🔐 Navigating to Dropbox login...")
            page.goto("https://www.dropbox.com/login")

            print("✍️ Waiting for email field...")
            page.wait_for_selector('input[name="login_email"]', timeout=10000000)
            print("✍️ Filling in credentials...")
            page.fill('input[name="login_email"]', "your_email_here")
            page.fill('input[name="login_password"]', "your_password_here")
            page.click('button[type="submit"]')

            time.sleep(5)  # give time to login
            # add scraping logic here...

        except Exception as e:
            print("❌ Error during automation:", e)
        finally:
            print("🧹 Closing browser...")
            browser.close()


if __name__ == "__main__":
    login_and_scrape_users()

