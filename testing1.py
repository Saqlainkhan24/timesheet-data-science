from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

import time

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/")

wait = WebDriverWait(driver, 10)
    # Wait for the username field to be visible
username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    
    # Enter credentials
username_field.send_keys("Admin")  # Default username for the demo
password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("admin123")  # Default password for the demo

    # Locate and click the login button
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

# Optional: Wait for a few seconds to see the result
time.sleep(5)

# Close the browser



driver.close