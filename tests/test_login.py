from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 30)

    # Siteye git
    driver.get("https://www.belgenet.com.tr/")

    # Demo seçimi
    wait.until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='menu']/ul/li[1]/a"))
    ).click()

    # Login
    wait.until(
        EC.visibility_of_element_located(
            (By.ID, "parolaSertifikaAccordion:uForm:txtUKullaniciAdi")
        )
    ).send_keys("botcu")

    driver.find_element(By.ID, "loginUSifre").send_keys("spider")

    wait.until(
        EC.element_to_be_clickable(
            (By.ID, "parolaSertifikaAccordion:uForm:girisYapButton")
        )
    ).click()

    # Login başarılı mı kontrol
    wait.until(
        EC.presence_of_element_located((By.ID, "topMenuForm2"))
    )

    driver.quit()
