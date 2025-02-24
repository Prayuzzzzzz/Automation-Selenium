from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import time
# Automatically download and set up WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open a website
driver.get("https://merolagani.com/")

driver.maximize_window()
time.sleep(5)
#dismiss alert
try:
    alert= Alert(driver)
    alert.dismiss()
except:
    print("no alert found")
#select market
market = driver.find_element(*(By.XPATH,"//a[normalize-space()='Market']"))
market.click()
time.sleep(5)
#select trading
trading = driver.find_element(By.XPATH,("//a[normalize-space()='Live Trading']"))
trading.click()
time.sleep(5)
#select ADBL
adbl = driver.find_element(By.XPATH,("//a[normalize-space()='ADBL']"))
adbl.click()
time.sleep(5)
#Scroll
driver.switch_to.window(driver.window_handles[1])
time.sleep(4)

driver.execute_script("window.scrollBy(0,500)")
time.sleep(5)
#price history
price_history = driver.find_element,(By.XPATH,("//a[@id='ctl00_ContentPlaceHolder1_CompanyDetail1_lnkHistoryTab']"))
price_history.click()
time.sleep(4)
# Close the browser
driver.quit()