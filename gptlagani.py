from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Open the website and maximize window
    driver.get("https://merolagani.com/")
    driver.maximize_window()
    time.sleep(5)

    # Select "Market" button and click
    market = driver.find_element(By.XPATH, "//a[normalize-space()='Market']")
    market.click()
    time.sleep(5)

    # Select "Live Trading" button and click
    trading = driver.find_element(By.XPATH, "//a[normalize-space()='Live Trading']")
    trading.click()
    time.sleep(5)

    # Select "ADBL" button and click
    adbl = driver.find_element(By.XPATH, "//a[normalize-space()='ADBL']")
    adbl.click()
    time.sleep(5)

    # Scroll the "ADBL" element into view
    driver.execute_script("arguments[0].scrollIntoView();", adbl)
    time.sleep(2)

    # Scroll to the bottom to load any dynamic content
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)

    # Optionally, scroll step by step if it's an infinite scroll page
    for _ in range(5):  # Adjust the range based on the content load
        driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(2)

finally:
    driver.quit()
