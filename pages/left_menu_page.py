from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LeftMenuPage(BasePage):

    # ===== MENÜ =====
    ISLEM_YAPTIKLARIM_HEADER = (By.XPATH, "//h3[normalize-space()='İşlem Yaptıklarım']")
    IMZALADIKLARIM_MENU = (By.XPATH, "//span[normalize-space()='İmzaladıklarım']")

    BIRIM_EVRAKLARI_HEADER = (By.XPATH, "//li[contains(@class,'birimEvraklari-icon')]//h3[contains(normalize-space(.),'Birim Evrakları')]")
    TESLIM_ALINMAYI_BEKLEYENLER_MENU = (By.XPATH, "//*[@id='leftMenuForm:leftMenuBirimEvraklari']/ul/li[2]")

    #TESLIM_ALINMAYI_BEKLEYENLER_MENU = (By.XPATH, "//a[contains(text(),'Teslim Alınmayı Bekleyenler')]")

    # ===== TABLO =====
    INBOX_TABLE = (By.ID, "mainInboxForm:inboxDataTable")
    INBOX_ROWS = (By.XPATH, "//*[@id='mainInboxForm:inboxDataTable_data']/tr")

    # ========================= ORTAK =========================
    def _wait_table_ready(self):
        self.wait_visible(self.INBOX_TABLE)
        self.wait.until(lambda d: len(d.find_elements(*self.INBOX_ROWS)) > 0)

    # ========================= İMZALADIKLARIM =========================
    def go_to_signed_documents(self):
        self.js_click(self.wait_clickable(self.ISLEM_YAPTIKLARIM_HEADER))
        self.js_click(self.wait_clickable(self.IMZALADIKLARIM_MENU))
        self._wait_table_ready()

    # ========================= TESLİM ALINMAYI BEKLEYENLER =========================
    # def go_to_teslim_alinmayi_bekleyenler(self):
    #     self.js_click(self.wait_clickable(self.ISLEM_YAPTIKLARIM_HEADER))
    #     self.js_click(self.wait_clickable(self.BIRIM_EVRAKLARI_HEADER))
    #     header = self.wait_clickable(self.BIRIM_EVRAKLARI_HEADER)
    #     self.driver.execute_script("arguments[0].scrollIntoView(true);", header)
    #     header.click()

    #     # Alt menü görünür olana kadar bekle
    #     submenu = self.wait_present(self.TESLIM_ALINMAYI_BEKLEYENLER_MENU)
    #     submenu.click()

    #     self.wait_visible(self.INBOX_TABLE)

    #     self.wait.until(
    #         lambda d: len(d.find_elements(*self.INBOX_ROWS)) > 0
    #     )
    
    def go_to_teslim_alinmayi_bekleyenler(self):
        # Header aç
        self.js_click(self.wait_clickable(self.ISLEM_YAPTIKLARIM_HEADER))

        header = self.wait_clickable(self.BIRIM_EVRAKLARI_HEADER)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", header)
        self.js_click(header)

        # Alt menüyü tıklayın
        submenu = self.wait_clickable(self.TESLIM_ALINMAYI_BEKLEYENLER_MENU)
        self.js_click(submenu)

        # Tabloyu bekleyin
        self._wait_table_ready()

      
    # ========================= İMZA TARİHİ VE GEREĞİNİN KONTROLÜ =========================
    def check_signature_and_geregi(self, expected_time, expected_geregi):
        rows = self.driver.find_elements(*self.INBOX_ROWS)

        for row in rows:
            row_text = row.text  # innerText yerine Selenium text daha stabil
            if expected_time in row_text and expected_geregi in row_text:
                return True
        return False

    # ========================= LOG =========================
    def log_signature(self, imza_zamani, secilen_geregi):
        with open("signature_log.txt", "a", encoding="utf-8") as f:
            f.write(f"[IMZA] {imza_zamani} | GEREĞİ: {secilen_geregi}\n")
            f.flush()
