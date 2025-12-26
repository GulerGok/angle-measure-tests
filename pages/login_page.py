from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    DEMO_BTN = (By.XPATH, "//*[@id='menu']/ul/li[1]/a")
    USERNAME = (By.ID, "parolaSertifikaAccordion:uForm:txtUKullaniciAdi")
    PASSWORD = (By.ID, "loginUSifre")
    LOGIN_BTN = (By.ID, "parolaSertifikaAccordion:uForm:girisYapButton")

    def open_demo(self):
        self.wait_clickable(self.DEMO_BTN).click()

    def login(self, username, password):
        self.wait_visible(self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.wait_clickable(self.LOGIN_BTN).click()
