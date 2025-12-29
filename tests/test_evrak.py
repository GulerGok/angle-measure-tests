from core.driver_factory import create_driver
from pages.evrak_page import EvrakPage
from pages.login_page import LoginPage
from pages.left_menu_page import LeftMenuPage


def test_evrak_flow():
    driver = create_driver()

    try:
        # Login
        login_page = LoginPage(driver)
        login_page.login()

        evrak_page = EvrakPage(driver)
        left_menu = LeftMenuPage(driver)

        # Evrak oluşturma
        evrak_page.create_document()
        evrak_page.select_folder()
        evrak_page.select_geregi()
        evrak_page.onay_akisi()
        evrak_page.fill_editor("XYZ")
        evrak_page.fill_ckeditor("Test Evrak içeriği buraya yazıldı")
        evrak_page.imza_ekle("Deneme İmza Metni")

        # EK DOSYA (case sabit, birebir path)
        file_path = r"C:\Users\MSI\Downloads\file-sample.doc"
        evrak_page.add_attachment(file_path=file_path)

        # İmzala
        imza_zamani = evrak_page.sign_document()
        assert imza_zamani is not None, "İmza işlemi başarısız"

        # İmzaladıklarım
        left_menu.go_to_signed_documents()

        # Doğrulama
        assert left_menu.check_signature_time(imza_zamani), \
            f"İmza zamanı bulunamadı: {imza_zamani}"

    finally:
        driver.quit()


if __name__ == "__main__":
    test_evrak_flow()
