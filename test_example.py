from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    
    broswer = playwright.chromium.launch(headless=False  ,slow_mo=500)

    page = broswer.new_page()

    page.goto("https://the-internet.herokuapp.com/")
    #page.screenshot(path="demo.png")
    page.click("text=Form Authentication")
    
    page.get_by_label("Username").fill("tomsmith")

    page.get_by_label("Password").fill("SuperSecretPassword!")

    page.get_by_role("button", name="Login").click()

    #page.get_by_role("button", name=("Logout")).click()

    broswer.close