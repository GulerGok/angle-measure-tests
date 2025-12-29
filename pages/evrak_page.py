from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import pyautogui, time
from datetime import datetime
class EvrakPage(BasePage):

    
    # ========================= MENU =========================
    CREATE_MENU = (By.ID, "topMenuForm2:ust:0:ustMenuEleman")
    CREATE_BTN = (By.LINK_TEXT, "Evrak Oluştur")

    # # ========================= KONU KODU =========================
    # KONU_KODU_INPUT = (By.XPATH, "//div[contains(@id,'konuKoduLov')]//input")
    # KONU_KODU_TREE_BTN = (By.XPATH, "//*[contains(@id,'konuKoduLov') and contains(@id,'treeButton')]")
    # KONU_KODU_DIALOG = (By.XPATH, "//*[contains(@id,'konuKoduLovlovDialogId')]")
    # KONU_KODU_ROOT = (By.XPATH, "//*[@id='yeniGidenEvrakForm:evrakBilgileriList:1:konuKoduLov:lovTree:1']/span/span[1]")
    # KONU_KODU_CHILD = (By.XPATH, "//*[@id='yeniGidenEvrakForm:evrakBilgileriList:1:konuKoduLov:lovTree:1_2']/span/span[3]")
    # KONU_KODU_CLOSE = (By.XPATH, "//*[@id='yeniGidenEvrakForm:evrakBilgileriList:1:konuKoduLov:lovOverlayPanelKapat']")

    # ========================= KLASÖR =========================
    # TREE_BTN = (By.XPATH,"//*[contains(@id,'eklenecekKlasorlerLov') and contains(@id,'treeButton')]")
    # TREE_ROOT = (By.XPATH,"//*[@id='yeniGidenEvrakForm:evrakBilgileriList:4:""eklenecekKlasorlerLov:lovTree:0']//span[contains(@class,'ui-tree-toggler')]")
    # TREE_ROOT2 = (By.XPATH,"//*[@id='yeniGidenEvrakForm:evrakBilgileriList:4:""eklenecekKlasorlerLov:lovTree:0_0']//span[contains(@class,'ui-tree-toggler')]")
    # TREE_ROOT3 = (By.XPATH, "//*[@id='yeniGidenEvrakForm:evrakBilgileriList:4:""eklenecekKlasorlerLov:lovTree:0_0_1']//span[contains(@class,'ui-tree-toggler')]")
    # TREE_CHILD = (By.XPATH,"//*[@id='yeniGidenEvrakForm:evrakBilgileriList:4:""eklenecekKlasorlerLov:lovTree:0_0_1_0']//span[contains(@class,'ui-treenode-label')]")
    # TREE_CLOSE = (By.XPATH,"//*[@id='yeniGidenEvrakForm:evrakBilgileriList:4:""eklenecekKlasorlerLov:lovOverlayPanelKapat']")
    #----
    # TREE_BTN = (By.XPATH,"//*[contains(@id,'eklenecekKlasorlerLov') and contains(@id,'treeButton')]")
    # TREE_ROOT = (By.XPATH,"//*[@id='yeniGidenEvrakForm:evrakBilgileriList:4:eklenecekKlasorlerLov:lovTree:0']//span[contains(@class,'ui-tree-toggler')]")
    # TREE_ROOT2 = (By.XPATH,"//*[@id='yeniGidenEvrakForm:evrakBilgileriList:4:eklenecekKlasorlerLov:lovTree:0_1']//span[contains(@class,'ui-tree-toggler')]")
    # TREE_ROOT3 = (By.XPATH, "//*[@id='yeniGidenEvrakForm:evrakBilgileriList:4:eklenecekKlasorlerLov:lovTree:0_1_1']//span[contains(@class,'ui-tree-toggler')]")
    # TREE_CHILD = (By.XPATH,"//*[@id='yeniGidenEvrakForm:evrakBilgileriList:4:eklenecekKlasorlerLov:lovTree:0_1_1_0']/span/span[3]/div")
    # TREE_CLOSE = (By.XPATH,"//*[@id='yeniGidenEvrakForm:evrakBilgileriList:4:""eklenecekKlasorlerLov:lovOverlayPanelKapat']")

    #========================= KLASÖR =========================
    TREE_BTN = (By.XPATH,"//*[contains(@id,'eklenecekKlasorlerLov') and contains(@id,'treeButton')]")
    TREE_CHILD = (By.XPATH,"//*[@id='yeniGidenEvrakForm:evrakBilgileriList:4:eklenecekKlasorlerLov:lovTree:2']/span/span[3]/div")
    TREE_CLOSE = (By.XPATH,"//*[@id='yeniGidenEvrakForm:evrakBilgileriList:4:""eklenecekKlasorlerLov:lovOverlayPanelKapat']")
    
    # ========================= GEREĞİ =========================
    GEREGI_BTN = (By.ID, "yeniGidenEvrakForm:evrakBilgileriList:20:geregiLov:treeButton")
    GEREGI_DIALOG = (By.XPATH, "//*[contains(@id,'geregiLovlovDialogId')]")
    GEREGI_ROOT = (By.XPATH, "//*[@id='yeniGidenEvrakForm:evrakBilgileriList:20:geregiLov:lovTree:0']/span/span[1]")
    GEREGI_CHILD = (By.XPATH, "//*[@id='yeniGidenEvrakForm:evrakBilgileriList:20:geregiLov:lovTree:0_1']/span/span[3]/div/span[1]")
    GEREGI_CLOSE = (By.ID, "yeniGidenEvrakForm:evrakBilgileriList:20:geregiLov:lovOverlayPanelKapat")

    # ========================= EDITOR =========================
    EDITOR_BTN = (By.ID, "yeniGidenEvrakForm:leftTab:uiRepeat:1:cmdbutton")
    EDITOR_UST_VERI_BTN = (By.ID, "yeniGidenEvrakForm:hitapUstVeriEkle")
    EDITOR_INPUT = (By.ID, "yeniGidenEvrakForm:hitapEkInplaceTextId")
    EDITOR_SAVE = (By.XPATH, "//*[@id='yeniGidenEvrakForm:j_idt10870']/span")

    # ========================= CKEDITOR =========================
    CKEDITOR_IFRAME = (By.XPATH, "//*[@id='cke_2_contents']/iframe")
    CKEDITOR_BODY = (By.TAG_NAME, "body")

    # ========================= EKLER ============================
    EKLER_PANEL = (By.ID, "yeniGidenEvrakForm:leftTab:uiRepeat:2:panelGrid")
    EKLER_BTN = (By.ID, "yeniGidenEvrakForm:leftTab:uiRepeat:2:cmdbutton")
    EKLER_TEXTAREA = (By.ID, "yeniGidenEvrakForm:evrakEkTabView:dosyaAciklama")
    EKLER_UPLOAD_BTN = (By.XPATH, "//*[@id='yeniGidenEvrakForm:evrakEkTabView:fileUploadButtonA']/div[1]/span")
    EKLER_ADD_BTN = (By.ID, "yeniGidenEvrakForm:evrakEkTabView:dosyaEkleButton")

    # ========================= İMZA EKLE =========================
    IMZA_INPLACE_BTN = (By.ID,"yeniGidenEvrakForm:imzacilarPanelUiId:0:""imzacilarPanelUiRepeatId:2:ImzacıUstVeriEkle")
    IMZA_INPUT = (By.XPATH,"//textarea[contains(@id,'imzacilarPanelUiRepeatId:2') and @maxlength='100']")
    IMZA_TAMAM_BTN = (By.XPATH,"//*[@id='yeniGidenEvrakForm:imzacilarPanelUiId:0:imzacilarPanelUiRepeatId:2:imzaciAdinaInplaceTamamButonID']")

    # =========================ONAY AKIŞI=========================
    ONAY_AKISI_BTN = (By.XPATH, "//*[contains(@id,'otomatikOnayAkisiEkle')]")
    HIYERARSIK_DIALOG = (By.XPATH, "//*[contains(@id,'hiyerarsikAkisOlusturDialog')]")
    ONAY_CHECKBOX = (By.XPATH, "//*[contains(@id,'otomatikAkisKullaniciBirimListId_null_checkbox')]")
    ONAY_OPTION_4 = (
        By.XPATH,
        "//*[@id='yeniGidenEvrakForm:hiyerarsikAkisOlusturForm:"
        "otomatikAkisKullaniciBirimListId_data']/tr[1]/td[6]/select/option[4]"
    )
    HIYERARSIK_KULLAN_BTN = (By.XPATH, "//*[contains(@id,'hiyerarsikAkisKullan')]")

    # ========================= EVRAK İMZALAMA ==================
    SIGN_TAB_BTN = (By.ID, "yeniGidenEvrakForm:rightTab:uiRepeat:2:cmdbutton")
    SIGN_DIALOG = (By.XPATH, "//*[@id='evrakImzalaDialog']")
    SIGN_CONFIRM_BTN = (By.XPATH, "//*[@id='imzalaForm:sayisalImzaConfirmDialogOpener']")
    SIGN_EVET_BTN = (By.XPATH, "//*[@id='imzalaForm:sayisalImzaConfirmForm:sayisalImzaEvetButton']")
    SIGN_DIALOG2 = (By.XPATH, "//*[@id='imzalaForm:j_idt2802']")


    # ============================METODLAR=============================

    def create_document(self):
        self.js_click(self.wait_clickable(self.CREATE_MENU))
        self.js_click(self.wait_clickable(self.CREATE_BTN))

    # def select_konu_kodu(self):
    #     konu_input = self.wait_present(self.KONU_KODU_INPUT)
    #     if not konu_input.get_attribute("value"):
    #         self.js_click(self.wait_clickable(self.KONU_KODU_TREE_BTN))
    #         self.wait_present(self.KONU_KODU_DIALOG)
    #         self.js_click(self.wait_present(self.KONU_KODU_ROOT))
    #         self.js_click(self.wait_present(self.KONU_KODU_CHILD))
    #         self.js_click(self.wait_clickable(self.KONU_KODU_CLOSE))

    def select_folder(self):
        self.js_click(self.wait_clickable(self.TREE_BTN))
        # self.js_click(self.wait_present(self.TREE_ROOT))
        # self.js_click(self.wait_present(self.TREE_ROOT2))
        # self.js_click(self.wait_present(self.TREE_ROOT3))
        self.js_click(self.wait_present(self.TREE_CHILD))
        self.js_click(self.wait_clickable(self.TREE_CLOSE))

    def select_geregi(self):
        self.js_click(self.wait_clickable(self.GEREGI_BTN))
        self.wait_present(self.GEREGI_DIALOG)
        self.js_click(self.wait_present(self.GEREGI_ROOT))
        self.js_click(self.wait_present(self.GEREGI_CHILD))
        self.js_click(self.wait_present(self.GEREGI_CLOSE))

    def onay_akisi(self):
        # Dialog aç
        self.js_click(self.wait_clickable(self.ONAY_AKISI_BTN))

        # Dialog görünür olana kadar bekle
        self.wait_present(self.HIYERARSIK_DIALOG)

        # Checkbox
        self.js_click(self.wait_present(self.ONAY_CHECKBOX))

        # Option (select içi)
        self.js_click(self.wait_present(self.ONAY_OPTION_4))

        # KRİTİK NOKTA
        # element_to_be_clickable KULLANMIYORUZ
        # çünkü DOM rerender oluyor
        kullan_btn = self.wait_present(self.HIYERARSIK_KULLAN_BTN)
        self.driver.execute_script("arguments[0].click();", kullan_btn)

    def fill_editor(self, text):
        self.js_click(self.wait_clickable(self.EDITOR_BTN))
        self.js_click(self.wait_clickable(self.EDITOR_UST_VERI_BTN))
        input_field = self.wait_visible(self.EDITOR_INPUT)
        input_field.clear()
        input_field.send_keys(text)
        self.js_click(self.wait_present(self.EDITOR_SAVE))

    def fill_ckeditor(self, text):
        iframe = self.wait_visible(self.CKEDITOR_IFRAME)
        self.driver.switch_to.frame(iframe)
        body = self.wait_visible(self.CKEDITOR_BODY)
        body.clear()
        body.send_keys(text)
        self.driver.switch_to.default_content()

    def imza_ekle(self, text):
        self.js_click(self.wait_clickable(self.IMZA_INPLACE_BTN))
        textarea = self.wait_visible(self.IMZA_INPUT)

        # temizle + JS ile yaz (PrimeFaces uyumlu)
        self.driver.execute_script(
            """
            arguments[0].value = '';
            arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
            """,
            textarea
        )

        self.driver.execute_script(
            """
            arguments[0].value = arguments[1];
            arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
            arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
            """,
            textarea,
            text
        )

        self.js_click(self.wait_clickable(self.IMZA_TAMAM_BTN))

    def add_attachment(
        self,
        description="Bu evrak için ek açıklama metni girildi.",
        file_path=None
    ):
        self.js_click(self.wait_clickable(self.EKLER_PANEL))
        self.js_click(self.wait_clickable(self.EKLER_BTN))

        textarea = self.wait_visible(self.EKLER_TEXTAREA)
        textarea.clear()
        textarea.send_keys(description)

        self.js_click(self.wait_clickable(self.EKLER_UPLOAD_BTN))

        if file_path:
            time.sleep(5)
            pyautogui.write(file_path)
            time.sleep(2)
            pyautogui.press("enter")
            time.sleep(2)
        self.js_click(self.wait_clickable(self.EKLER_ADD_BTN))

    
    # def sign_document(self):
    #         # SIGN TAB'ı aç
    #         self.js_click(self.wait_clickable(self.SIGN_TAB_BTN))

    #         try:
    #             # İlk confirm dialog görünür olana kadar bekle
    #             self.wait_visible(self.SIGN_DIALOG)

    #             # İlk formdaki "İmzala" butonuna tıkla
    #             self.js_click(self.wait_clickable(self.SIGN_CONFIRM_BTN))

    #             # İkinci form (Sayısal İmzala) görünür olana kadar bekle
    #             self.wait_visible(self.SIGN_DIALOG2)

    #             time.sleep(2)
    #             # "Evet" butonu tıklanabilir olana kadar bekle
    #             evet_btn = self.wait_clickable(self.SIGN_EVET_BTN)

    #             # Butonu görünür yapmak için scrollIntoView ve JS tıklaması
    #             self.driver.execute_script(
    #                 "arguments[0].scrollIntoView(true); arguments[0].click();", evet_btn
    #             )

    #             time.sleep(2)
    #             # İkinci form DOM'dan kaybolana kadar bekle
    #             self.wait.until(EC.invisibility_of_element_located(self.SIGN_DIALOG2))

    #         except TimeoutException:
    #             print("İmza confirm dialogu açılamadı veya kapanmadı.")
        


    def sign_document(self):
        try:
            # 1️⃣ SIGN TAB
            self.js_click(self.wait_clickable(self.SIGN_TAB_BTN))

            # 2️⃣ İlk dialog (İmzala)
            self.wait_visible(self.SIGN_DIALOG)

            # 3️⃣ "İmzala" butonu
            self.js_click(self.wait_clickable(self.SIGN_CONFIRM_BTN))

            # 4️⃣ Sayısal imza dialogu
            self.wait_visible(self.SIGN_DIALOG2)

            # 5️⃣ "Evet" butonu
            evet_btn = self.wait_clickable(self.SIGN_EVET_BTN)
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});", evet_btn
            )
            self.driver.execute_script("arguments[0].click();", evet_btn)

            # 6️⃣ Dialog tamamen kapandı mı?
            self.wait.until(
                EC.invisibility_of_element_located(self.SIGN_DIALOG2)
            )

            # 7️⃣ AJAX tamamlandı mı? (PrimeFaces güvenliği)
            self.wait.until(
                lambda d: d.execute_script(
                    "return window.jQuery != undefined && jQuery.active === 0"
                )
            )

            # 8️⃣ İmza zamanı (tek referans)
            imza_zamani = datetime.now().strftime("%d.%m.%Y %H:%M")
            print(f"✅ İmza tamamlandı: {imza_zamani}")

            self.save_signature_info(imza_zamani)
            return imza_zamani

        except TimeoutException as e:
            print("❌ İmza akışı timeout oldu.")
            print(e)
            return None


    def save_signature_info(self, imza_zamani):
        with open("signature_log.txt", "a", encoding="utf-8") as f:
            f.write(f"[IMZA] {imza_zamani}\n")
            f.flush()
