from selenium import webdriver


def get_driver():

    driver = webdriver.Edge()

    driver.maximize_window()
    driver.implicitly_wait(10)

    return driver