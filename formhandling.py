from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Set up WebDriver for Edge
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

# Provide the website URL
url = "https://formy-project.herokuapp.com/form"
driver.get(url)
driver.maximize_window()
time.sleep(2)

# Locate and fill in the text fields
firstname = driver.find_element(By.XPATH, "//input[@id='first-name']")
lastname = driver.find_element(By.XPATH, "//input[@id='last-name']")
job_title = driver.find_element(By.XPATH, "//input[@id='job-title']")
education_level = driver.find_element(By.XPATH, "//input[@id='radio-button-2']")  # College
sex = driver.find_element(By.XPATH, "//input[@id='checkbox-1']")  # Male

firstname.send_keys("Roman")
time.sleep(1)
lastname.send_keys("Reigns")
time.sleep(1)
job_title.send_keys("QA")
time.sleep(1)

# Select education level (College)
education_level.click()
time.sleep(1)

# Scroll down
driver.execute_script("window.scrollBy(0,400)")

# Select gender (Male)
sex.click()
time.sleep(1)

# Select Years of Experience from dropdown
year_dropdown = Select(driver.find_element(By.XPATH, "//select[@id='select-menu']"))
year_dropdown.select_by_visible_text("0-1")
time.sleep(1)

# Select Date
date_field = driver.find_element(By.XPATH, "//input[@id='datepicker']")
date_field.send_keys("02/17/2025")
time.sleep(1)

# Click Submit button
submit_button = driver.find_element(By.XPATH, "//a[text()='Submit']")
submit_button.click()

# Wait for the form submission to complete
time.sleep(3)

# Quit the driver
driver.quit()
