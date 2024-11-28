from selenium import webdriver

# Launch the Chrome browser
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://www.example.com")

#driver.save_screenshot("full_page_screenshot.png")

# Locate a specific element on the page
element = driver.find_element_by_id("element-id")

# Capture a screenshot of the specific element
#element.screenshot("element_screenshot.png")

# Close the browser
driver.quit()
