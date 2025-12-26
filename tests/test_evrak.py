from core.driver_factory import create_driver
from pages.evrak_page import EvrakPage
from pages.login_page import LoginPage
import time
from utils.helpers import resolve_real_path


def test_evrak_flow():
    driver = create_driver()

    # Login (ön koşul)
    login_page = LoginPage(driver)
    login_page.login()

    # Evrak işlemleri
    evrak_page = EvrakPage(driver)

    evrak_page.create_document()
    evrak_page.select_konu_kodu()
    evrak_page.select_folder()
    evrak_page.select_geregi()
    evrak_page.onay_akisi()
    evrak_page.fill_editor("XYZ")
    evrak_page.fill_ckeditor("Test Evrak içeriği buraya yazıldı")
    evrak_page.imza_ekle("Deneme İmza Metni")

    file_path = resolve_real_path(
        r"C:\Users\MSI\Downloads\file-sample.doc"
    )
    
    print(file_path)

    evrak_page.add_attachment(file_path=file_path)
    evrak_page.sign_document()

    time.sleep(5)
    driver.quit()


if __name__ == "__main__":
    test_evrak_flow()
