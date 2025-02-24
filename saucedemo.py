from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By

import time
#set up a driver installation
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))


#provide a website
url = "https://www.saucedemo.com/"


driver.get(url)
driver.maximize_window()
time.sleep(2)

username = driver.findElement(By.xpath("//input[@id='user-name']"))
password = driver.findElement(By.xpath("//input[@id='password']"))
login_button = driver.findElement(By.xpath("//input[@id='login-button']"))

username.send_keys("standard_user")
time.sleep(2)

password.send_keys("secret_sauce")
time.sleep(2)

login_button.click()

title = driver.current_url

if (title== "https://www.saucedemo.com/inventory.html"):
    print("Login Successful")
else:
    print("Login Unsuccessful")
 
time.sleep(3)
driver.quit()