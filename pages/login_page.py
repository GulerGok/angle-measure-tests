from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    URL = "https://www.belgenet.com.tr/"

    DEMO_BTN = (By.XPATH, "//*[@id='menu']/ul/li[1]/a")
    USERNAME_INPUT = (
        By.ID,
        "parolaSertifikaAccordion:uForm:txtUKullaniciAdi"
    )
    PASSWORD_INPUT = (By.ID, "loginUSifre")
    LOGIN_BTN = (
        By.ID,
        "parolaSertifikaAccordion:uForm:girisYapButton"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def login(self, username="botcu", password="spider"):
        self.driver.get(self.URL)

        self.wait.until(
            EC.element_to_be_clickable(self.DEMO_BTN)
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(self.USERNAME_INPUT)
        ).send_keys(username)

        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BTN)
        ).click()
