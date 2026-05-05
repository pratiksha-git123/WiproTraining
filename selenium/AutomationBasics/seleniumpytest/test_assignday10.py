import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

#---------------------------------------Exercise1-----------------------------------------
service = Service()
driver = webdriver.Chrome(service=service)

driver.get("https://www.amazon.in")
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, "nav-logo-sprites")))
title = driver.title
print("Page Title:", title)
assert "Amazon" in title
mobiles = wait.until(
    EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Mobile"))
)
mobiles.click()
time.sleep(2)
driver.back()
time.sleep(2)

#------------------------------------------Exercise2-----------------------------------------
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.clear()
search_box.send_keys("Wireless Headphones")
search_button = driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']")
search_button.click()
result_text = driver.find_element(By.XPATH, "//span[contains(text(), 'results')]").text
assert "results" in result_text.lower()

#-------------------------------------------Exercise3------------------------------------------
# driver = webdriver.Chrome()
# driver.maximize_window()
driver.implicitly_wait(10)
# driver.get("https://www.amazon.in")
# time.sleep(2)
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.clear()
search_box.send_keys("Dell i5 Laptop")
search_box.send_keys(Keys.ENTER)
wait = WebDriverWait(driver, 15)
# wait.until(
#     EC.presence_of_all_elements_located((By.XPATH, "//div[@data-component-type='s-search-result']"))
# )
first_product = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//div[@data-component-type='s-search-result']"))
)
# driver.execute_script("arguments[0].scrollIntoView();", first_product)
first_product.click()
# print("Successfully clicked first product")
# wait.until(EC.presence_of_element_located((By.ID, "productTitle")))
# print("Product Page Title:", driver.title)
# driver.quit()
#---------------------------------------------Exercise4-----------------------------------------
driver.get("https://www.amazon.in")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
about_us = driver.find_element(By.CSS_SELECTOR, "a[href*='aboutamazon']")
about_us.click()
time.sleep(3)
element = driver.find_element(By.LINK_TEXT, "Careers")
print("Element text:", element.text)

#---------------------------------------------Exercise5------------------------------------------
service = Service()
driver = webdriver.Chrome(service=service)

try:
    driver.get("https://www.amazon.in")
    wait = WebDriverWait(driver, 20)

    # Search for Smart Watches
    search_box = wait.until(
        EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
    )
    search_box.clear()
    search_box.send_keys("Smart Watches")
    search_box.send_keys(Keys.ENTER)

    # Wait for results to load
    results = wait.until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//div[@data-component-type='s-search-result']")
        )
    )

    # Scroll to load Brand filter
    driver.execute_script("window.scrollBy(0, 600);")

    # Wait for Brand section
    wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Brand']")))

    # Select a brand dynamically (first available)
    brands = wait.until(
        EC.presence_of_all_elements_located((By.XPATH, "//li[@aria-label]"))
    )

    brand_checkbox = None
    for b in brands:
        try:
            checkbox = b.find_element(By.XPATH, ".//i")
            brand_checkbox = checkbox
            break
        except:
            continue

    if brand_checkbox is None:
        raise Exception("No brand checkbox found")

    # Store old results for synchronization
    first_product_before = results[0]

    # Click brand filter
    driver.execute_script("arguments[0].click();", brand_checkbox)

    # Wait for page refresh
    wait.until(EC.staleness_of(first_product_before))

    # Wait for updated results
    updated_results = wait.until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//div[@data-component-type='s-search-result']")
        )
    )

    # Count products
    print("Number of products after applying brand filter:", len(updated_results))

finally:
    # Close browser properly
    driver.quit()
