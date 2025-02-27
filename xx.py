from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# Open a webpage to test
url="https://filebin.net"
driver.get(url)
driver.maximize_window()
time.sleep(5)
select_file = driver.find_element(By.XPATH,("//input[@id='fileField']"))
select_file.send_keys("C:/Users/ACER/Downloads/download.jpg")
time.sleep(5)
driver.quit()