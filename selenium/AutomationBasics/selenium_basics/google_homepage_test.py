from time import sleep
from selenium import webdriver
from selenium.webdriver.ie.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager
browser = input("What browser you want to use?")
match (browser.lower()):
     case 'chrome':
         driver = webdriver.Chrome(service=Service('../resources/chromedriver.exe'))
     case 'edge':
         driver = webdriver.Edge(service=Service('../resources/msedgedriver.exe'))
     case _ :
         print("Unknown driver - Not Available")
         driver = webdriver.Edge(service=Service('../resources/msedgedriver.exe'))
# driver = webdriver.Edge(service=Service('../resources/msedgedriver.exe'))
# (EdgeChromiumDriverManager().install()))
driver.get("https://www.google.com")
pagetitle = driver.title
if pagetitle == 'Google':
    print("Google Homepage loaded - Pass")
else:
    print("Google Homepage NOT loaded - Fail")
sleep(3)
driver.quit()
