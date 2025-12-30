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

        # Evrak No ve Screenshot al
        evrak_no = left_menu.get_evrak_no_from_imzaladiklarim()
        screenshot_imzaladiklarim = left_menu.take_screenshot("imzaladiklarim")
        left_menu.log_list_status(
            "İMZALADIKLARIM",
            evrak_no,
            f"| İmza Zamanı: {imza_zamani} | Gereği: {secilen_geregi} | Screenshot: {screenshot_imzaladiklarim}"
        )
        print(f"İmzaladıklarım listesinde kayıt görüldü. Screenshot: {screenshot_imzaladiklarim}")

        # ================= TESLİM ALINMAYI BEKLEYENLER =================
        left_menu.check_evrak_no_in_teslim_list(evrak_no, take_ss=False)

        # Tablo tamamen yüklendikten sonra screenshot al
        screenshot_teslim = left_menu.take_screenshot("teslim_listesi")
        left_menu.log_list_status(
            "TESLİM ALINMAYI BEKLEYENLER",
            evrak_no,
            f"| Screenshot: {screenshot_teslim}"
        )
        print(f"Teslim Alınmayı Bekleyenler listesinde evrak bulundu. Screenshot: {screenshot_teslim}")

        print("TEST BAŞARIYLA TAMAMLANDI")

    finally:
        input("Test bitti. Tarayıcıyı kapatmak için Enter'a bas...")
        driver.quit()


if __name__ == "__main__":
    test_evrak_flow()
