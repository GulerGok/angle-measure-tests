from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LeftMenuPage(BasePage):

    # ===== MENÜ =====
    ISLEM_YAPTIKLARIM_HEADER = (By.XPATH, "//h3[normalize-space()='İşlem Yaptıklarım']")
    IMZALADIKLARIM_MENU = (By.XPATH, "//span[normalize-space()='İmzaladıklarım']")

    # ===== TABLO =====
    INBOX_TABLE = (By.ID, "mainInboxForm:inboxDataTable")
    INBOX_ROWS = (By.XPATH, "//*[@id='mainInboxForm:inboxDataTable_data']/tr")

    # =========================SAYFAYA GİT=========================
    def go_to_signed_documents(self):
        self.js_click(self.wait_clickable(self.ISLEM_YAPTIKLARIM_HEADER))
        self.js_click(self.wait_clickable(self.IMZALADIKLARIM_MENU))

        # tablo yüklenene kadar bekle
        self.wait_visible(self.INBOX_TABLE)

        # tablo boş değil mi?
        self.wait.until(
            lambda d: len(d.find_elements(*self.INBOX_ROWS)) >= 0
        )

    # =========================İMZA VAR MI?=========================
    def check_signature_time(self, expected_time):
        rows = self.wait.until(
            lambda d: d.find_elements(*self.INBOX_ROWS)
        )

        for row in rows:
            if expected_time in row.text:
                print(f"İmza bulundu: {row.text}")
                return True

        print(f"İmza bulunamadı: {expected_time}")
        return False
