from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LeftMenuPage(BasePage):

    # ===== MENÜ =====
    ISLEM_YAPTIKLARIM_HEADER = (By.XPATH, "//h3[normalize-space()='İşlem Yaptıklarım']")
    IMZALADIKLARIM_MENU = (By.XPATH, "//span[normalize-space()='İmzaladıklarım']")

    # ===== TABLO =====
    INBOX_TABLE = (By.ID, "mainInboxForm:inboxDataTable")
    INBOX_ROWS = (By.XPATH, "//*[@id='mainInboxForm:inboxDataTable_data']/tr")

    # ========================= SAYFAYA GİT =========================
    def go_to_signed_documents(self):
        self.js_click(self.wait_clickable(self.ISLEM_YAPTIKLARIM_HEADER))
        self.js_click(self.wait_clickable(self.IMZALADIKLARIM_MENU))

        # tablo yüklendi mi?
        self.wait_visible(self.INBOX_TABLE)

        # en az 1 kayıt gelmesini bekle
        self.wait.until(
            lambda d: len(d.find_elements(*self.INBOX_ROWS)) > 0
        )

    # ========================= İMZA + GEREĞİ =========================
    def check_signature_and_geregi(self, expected_time, expected_geregi):
        rows = self.wait.until(
            lambda d: d.find_elements(*self.INBOX_ROWS)
        )

        for row in rows:
            row_text = self.driver.execute_script(
                "return arguments[0].innerText;", row
            )

            if expected_time in row_text and expected_geregi in row_text:
                print("İmza + gereği eşleşti")
                return True

        print("İmza veya gereği eşleşmedi")
        return False


    def log_signature(self, imza_zamani, secilen_geregi):
        with open("signature_log.txt", "a", encoding="utf-8") as f:
            f.write(f"[IMZA] {imza_zamani} | GEREĞİ: {secilen_geregi}\n")
            f.flush()
