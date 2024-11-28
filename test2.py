import re
from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:
    
    broswer = playwright.chromium.launch(headless=False  ,slow_mo=500)

    page = broswer.new_page()

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Locate the username field and enter the username
    page.fill("input[name='username']", "Admin")  # Default username for the demo

    # Locate the password field and enter the password
    page.fill("input[name='password']", "admin123")  # Default password for the demo

    # Click the login button
    page.click("button[type='submit']")

