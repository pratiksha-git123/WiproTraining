import time
from re import search

from selenium.webdriver.ie.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Edge(service=Service("../resources/msedgedriver.exe"))

driver.get("https://www.google.com")
driver.implicitly_wait(5)

# search_box = driver.find_element(By.NAME, "q")
# search_box.send_keys("selenium")
# googlesearch_button = driver.find_element(By.NAME, "btnK")
# googlesearch_button.click()

#---------------------------------------------------------------------------------------------------

# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
#
# wait = WebDriverWait(driver, 10)
#
# search_box = wait.until(EC.visibility_of_element_located((By.NAME, "q")))
# search_box.send_keys("Explicit Wait")
#
# googlesearch_button = wait.until(EC.element_to_be_clickable((By.NAME, "btnK")))
# googlesearch_button.click()

#-----------------------------------------------------------------------------------------------

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchDriverException

wait = WebDriverWait(driver, timeout=10, poll_frequency=0.1,
                     ignored_exceptions=[NoSuchDriverException])

search_box = wait.until(EC.visibility_of_element_located((By.NAME, "q")))
search_box.send_keys("Explicit Wait")

imfl_button = wait.until(EC.element_to_be_clickable((By.NAME, "btnI")))
imfl_button.click()
driver.quit()
