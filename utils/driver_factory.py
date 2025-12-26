from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def create_driver(headless: bool = False):
    options = Options()

    if headless:
        options.add_argument("--headless=new")

    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    return driver
