from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Automatically download and set up WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open a website
driver.get("https://merolagani.com/")

# Print page title
print(driver.title)

# Close the browser
driver.quit()