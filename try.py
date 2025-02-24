from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# Open a webpage to test
url="https://formy-project.herokuapp.com/form"
driver.get(url)

driver.maximize_window()
firstName=driver.find_element(By.ID, "first-name")
firstName.send_keys("bikram")
lastName=driver.find_element(By.ID,"last-name")
lastName.send_keys("Rana")





time.sleep(5)
driver.quit()