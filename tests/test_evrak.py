from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import os

from pages.evrak_page import EvrakPage


def resolve_real_path(path: str) -> str:
    """
    Dosya yolunu büyük/küçük harf duyarsız şekilde
    diskten gerçek adıyla bulur.
    """
    directory, filename = os.path.split(path)

    if not os.path.isdir(directory):
        raise FileNotFoundError(f"Klasör bulunamadı: {directory}")

    for f in os.listdir(directory):
        if f.lower() == filename.lower():
            return os.path.join(directory, f)

    raise FileNotFoundError(f"Dosya bulunamadı: {filename}")


def test_evrak_flow():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 30)

    # 1. Siteye git
    driver.get("https://www.belgenet.com.tr/")

    # 2. Demo seçimi
    wait.until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='menu']/ul/li[1]/a"))
    ).click()

    # 3. Login
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

    # 4. Evrak işlemleri
    evrak_page = EvrakPage(driver)

    evrak_page.create_document()
    evrak_page.select_konu_kodu()
    evrak_page.select_folder()
    evrak_page.select_geregi()
    evrak_page.onay_akisi()
    evrak_page.fill_editor("XYZ")
    evrak_page.fill_ckeditor("Test Evrak içeriği buraya yazıldı")
    evrak_page.imza_ekle("Deneme İmza Metni")

    # DOSYA YOLU GÜVENLİ HALE GETİRİLİYOR
    file_path = resolve_real_path(
        r"C:\Users\MSI\Downloads\file-sample_100kB.doc"
    )

    evrak_page.add_attachment(file_path=file_path)

    evrak_page.sign_document()

    # 5. Çıkış
    time.sleep(5)
    driver.quit()


if __name__ == "__main__":
    test_evrak_flow()
