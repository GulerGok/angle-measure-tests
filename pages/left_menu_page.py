from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time
import re
import os

class LeftMenuPage(BasePage):

    # ===== MENÜ =====
    ISLEM_YAPTIKLARIM_HEADER = (By.XPATH, "//h3[normalize-space()='İşlem Yaptıklarım']")
    IMZALADIKLARIM_MENU = (By.XPATH, "//span[normalize-space()='İmzaladıklarım']")
    BIRIM_EVRAKLARI_HEADER = (By.XPATH, "//li[contains(@class,'birimEvraklari-icon')]//h3[contains(normalize-space(.),'Birim Evrakları')]")
    TESLIM_ALINMAYI_BEKLEYENLER_MENU = (
        By.XPATH, "//span[contains(normalize-space(.),'Teslim Alınmayı Bekleyenler')]"
    )

    # ===== TABLO =====
    INBOX_TABLE = (By.ID, "mainInboxForm:inboxDataTable")
    INBOX_ROWS = (By.XPATH, "//*[@id='mainInboxForm:inboxDataTable_data']/tr")

    # ========================= ORTAK =========================
    def _wait_table_ready(self, timeout=30):
        """Tablo render olana kadar bekle"""
        table = self.wait.until(EC.visibility_of_element_located(self.INBOX_TABLE))
        WebDriverWait(self.driver, timeout).until(
            lambda d: any(r.is_displayed() and r.text.strip() != "" for r in d.find_elements(*self.INBOX_ROWS))
        )

    # ========================= İMZALADIKLARIM =========================
    def go_to_signed_documents(self):
        self.js_click(self.wait_clickable(self.ISLEM_YAPTIKLARIM_HEADER))
        self.js_click(self.wait_clickable(self.IMZALADIKLARIM_MENU))
        self._wait_table_ready()

    def get_evrak_no_from_imzaladiklarim(self):
        rows = self.driver.find_elements(*self.INBOX_ROWS)
        for row in rows:
            match = re.search(r"No:\s*([\d\-\.\w]+)", row.text)
            if match:
                return match.group(1).strip()
        raise ValueError("İmzaladıklarım listesinde Evrak No bulunamadı.")

    # ========================= TESLİM ALINMAYI BEKLEYENLER =========================
    def go_to_teslim_alinmayi_bekleyenler(self):
        self.js_click(self.wait_clickable(self.ISLEM_YAPTIKLARIM_HEADER))
        header = self.wait_clickable(self.BIRIM_EVRAKLARI_HEADER)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", header)
        self.js_click(header)

        submenu = self.wait.until(EC.element_to_be_clickable(self.TESLIM_ALINMAYI_BEKLEYENLER_MENU))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", submenu)
        self.js_click(submenu)

        self._wait_table_ready()

    def check_evrak_no_in_teslim_list(self, evrak_no, timeout_seconds=60, interval_seconds=2, take_ss=True):
        """Teslim listesinde evrak no kontrolü ve tablo screenshot"""
        self.go_to_teslim_alinmayi_bekleyenler()
        start = time.time()
        found = False

        while time.time() - start < timeout_seconds:
            for row in self.driver.find_elements(*self.INBOX_ROWS):
                if evrak_no in row.text:
                    found = True
                    break
            if found:
                break
            time.sleep(interval_seconds)

        if not found:
            raise AssertionError(f"Evrak No='{evrak_no}' Teslim Alınmayı Bekleyenler listesinde bulunamadı.")

        if take_ss:
            path = self.take_screenshot(f"teslim_listesi_{evrak_no.replace('.', '_')}")
            print(f"Screenshot: {path}")

        return True

    # ========================= İMZA VE GEREĞİ KONTROL =========================
    def check_signature_and_geregi(self, expected_time, expected_geregi):
        rows = self.driver.find_elements(*self.INBOX_ROWS)
        for row in rows:
            if expected_time in row.text and expected_geregi in row.text:
                return True
        return False

    # ========================= LOG =========================
    def log_signature(self, imza_zamani, secilen_geregi):
        os.makedirs("logs", exist_ok=True)
        with open("logs/signature_log.txt", "a", encoding="utf-8") as f:
            f.write(f"[{datetime.now().strftime('%d.%m.%Y %H:%M:%S')}] [IMZA] {imza_zamani} | GEREĞİ: {secilen_geregi}\n")
            f.flush()

    def log_list_status(self, list_name, evrak_no, extra_info=""):
        os.makedirs("logs", exist_ok=True)
        with open("logs/evrak_flow_log.txt", "a", encoding="utf-8") as f:
            f.write(f"[{datetime.now().strftime('%d.%m.%Y %H:%M:%S')}] [{list_name}] Evrak No: {evrak_no} {extra_info}\n")
            f.flush()

    # ========================= SCREENSHOT =========================
    def take_screenshot(self, name):
        os.makedirs("screenshots", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = f"screenshots/{name}_{timestamp}.png"
        self.driver.save_screenshot(path)
        return path
