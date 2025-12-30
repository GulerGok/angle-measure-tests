# tests/test_evrak_flow.py
from core.driver_factory import create_driver
from pages.evrak_page import EvrakPage
from pages.login_page import LoginPage
from pages.left_menu_page import LeftMenuPage

def test_evrak_flow():
    driver = create_driver()

    try:
        # ================= LOGIN =================
        login_page = LoginPage(driver)
        login_page.login()

        evrak_page = EvrakPage(driver)
        left_menu = LeftMenuPage(driver)

        # ================= EVRAK OLUŞTUR =================
        evrak_page.create_document()
        evrak_page.select_folder()
        secilen_geregi = evrak_page.select_geregi()
        evrak_page.onay_akisi()
        evrak_page.fill_editor("XYZ")
        evrak_page.fill_ckeditor("Test Evrak içeriği")
        evrak_page.imza_ekle("Deneme İmza Metni")

        # ================= EK =================
        evrak_page.add_attachment(
            file_path=r"C:\Users\MSI\Downloads\file-sample.doc"
        )

        # ================= İMZA =================
        imza_zamani = evrak_page.sign_document()
        assert imza_zamani is not None, "İmza başarısız"

        # ================= LOG =================
        left_menu.log_signature(imza_zamani, secilen_geregi)

        # ================= İMZALADIKLARIM =================
        left_menu.go_to_signed_documents()
        assert left_menu.check_signature_and_geregi(
            imza_zamani,
            secilen_geregi
        ), f"Evrak bulunamadı → {imza_zamani} | {secilen_geregi}"

        print("İmzaladıklarım listesinde kayıt görüldü.")

        # ================= TESLİM ALINMAYI BEKLEYENLER =================
        # Evrak No kontrolünü kullanarak fail durumunu yakala
        left_menu.check_evrak_no_in_teslim_list(timeout_seconds=60, interval_seconds=5)

        print("Teslim Alınmayı Bekleyenler listesinde evrak bulundu.")
        print("TEST BAŞARIYLA TAMAMLANDI")

    finally:
        input("Test bitti. Tarayıcıyı kapatmak için Enter'a bas...")
        driver.quit()


if __name__ == "__main__":
    test_evrak_flow()
