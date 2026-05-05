from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

#start driver
driver = webdriver.Edge()
driver.maximize_window()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")
time.sleep(2)

#-------------------------------------TEXT INPUT--------------------------------------------
text_input = driver.find_element(By.ID, "my-text-id")
text_input.clear()
text_input.send_keys("Selenium WebDriver Demo")

#--------------------------------------PASSWORD INPUT-----------------------------------------
password_input = driver.find_element(By.NAME, "my-password")
password_input.clear()
password_input.send_keys("secret123")

#---------------------------------------TEXT AREA----------------------------------------------
textarea = driver.find_element(By.NAME, "my-textarea")
textarea.clear()
textarea.send_keys("This is a sample message.")

#-----------------------------------------CHECKBOX----------------------------------------------
checkbox = driver.find_element(By.ID, "my-check-2")
checkbox.click()

#-----------------------------------------RADIO BUTTON-------------------------------------------
radio = driver.find_element(By.ID, "my-radio-2")
radio.click()

#-----------------------------------------DROPDOWN------------------------------------------------
dropdown = driver.find_element(By.NAME, "my-select")
dropdown.click()
option = driver.find_element(By.CSS_SELECTOR, "select[name='my-select'] option[value='2']")
option.click()

#-----------------------------------------MULTI-SELECT---------------------------------------------
multi_select = driver.find_element(By.NAME, "my-datalist")
multi_select.send_keys('NEW YORK')

#------------------------------------------FILE-UPLOAD----------------------------------------------
file_upload = driver.find_element(By.NAME, "my-file")
file_upload.send_keys("C:\\WiproTraining\\selenium\\AutomationBasics\\selenium_basics")

#------------------------------------------RANGE SLIDER----------------------------------------------
range_slider = driver.find_element(By.NAME, "my-range")
driver.execute_script("arguments[0].value = 10;", range_slider)

#------------------------------------------COLOR PICKER----------------------------------------------
color_picker = driver.find_element(By.NAME, "my-colors")
color_picker.send_keys("#00ff00")

#-------------------------------------------DATE -----------------------------------------------------
date_input = driver.find_element(By.NAME, "my-date")
date_input.send_keys("2025-12-25")

#--------------------------------------------SUBMIT BUTTON---------------------------------------------
submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
time.sleep(20)
submit_btn.click()

time.sleep(10)
driver.quit()