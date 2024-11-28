import re
from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:
    
    broswer = playwright.chromium.launch(headless=False  ,slow_mo=500)

    page = broswer.new_page()


    page.goto("https://katalon-demo-cura.herokuapp.com/")

    page.click("text= Make Appointment")

    page.get_by_label("Username").fill("John Doe")

    page.get_by_label("Password").fill("ThisIsNotAPassword")

    page.get_by_role("button", name="Login").click()

    facility_dropdown = page.get_by_role("combobox", name="#combo_facility")

# Option 2 (Using CSS selector directly):
    facility_dropdown = page.locator("#combo_facility")

    facility_dropdown.select_option("Hongkong CURA Healthcare Center")

    #radio_button = page.get_by_label("Healthcare Program")

    # Ensure the page is still open before checking
    #if page.is_closed():
    #raise Exception("Page is closed! Cannot interact with elements.")

    # Now it's safe to interact with the element
    #radio_button.click



    page.get_by_role('input[name="Healthcare Program"][value="Medicaid"]')

    page.fill("#txt_visit_date", "") 
    
    page.type("#txt_visit_date", "20/11/2024")

    page.get_by_label("Comment").fill("My name is khan")

    page.get_by_role("button", name="Book Appointment").click()
    
broswer.close
