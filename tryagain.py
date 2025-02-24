from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# Open a webpage to test
url="https://www.facebook.com"
driver.get(url)
time.sleep(5)
username = driver.find_element(*(By.XPATH,"//input[@id='email']"))
username.send_keys("hello")
driver.execute_script("window.scrollBy(0,200)")
time.sleep(5)
driver.quit()