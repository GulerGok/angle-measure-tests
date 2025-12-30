from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
import time
import re

class LeftMenuPage(BasePage):

    # ===== MENÜ =====
    ISLEM_YAPTIKLARIM_HEADER = (By.XPATH, "//h3[normalize-space()='İşlem Yaptıklarım']")
    IMZALADIKLARIM_MENU = (By.XPATH, "//span[normalize-space()='İmzaladıklarım']")

    BIRIM_EVRAKLARI_HEADER = (By.XPATH, "//li[contains(@class,'birimEvraklari-icon')]//h3[contains(normalize-space(.),'Birim Evrakları')]")
    TESLIM_ALINMAYI_BEKLEYENLER_MENU = (By.XPATH, "/html/body/div[8]/div[2]/form/div[5]/ul/li[2]")

    # ===== TABLO =====
    INBOX_TABLE = (By.ID, "mainInboxForm:inboxDataTable")
    INBOX_ROWS = (By.XPATH, "//*[@id='mainInboxForm:inboxDataTable_data']/tr")

    # ========================= ORTAK =========================
    def _wait_table_ready(self):
        self.wait_visible(self.INBOX_TABLE)
        self.wait.until(lambda d: any(r.text.strip() != "" for r in d.find_elements(*self.INBOX_ROWS)))

    # ========================= İMZALADIKLARIM =========================
    def go_to_signed_documents(self):
        self.js_click(self.wait_clickable(self.ISLEM_YAPTIKLARIM_HEADER))
        self.js_click(self.wait_clickable(self.IMZALADIKLARIM_MENU))
        self._wait_table_ready()

    # ========================= TESLİM ALINMAYI BEKLEYENLER =========================
    def go_to_teslim_alinmayi_bekleyenler(self):
        self.js_click(self.wait_clickable(self.ISLEM_YAPTIKLARIM_HEADER))
        self.js_click(self.wait_clickable(self.BIRIM_EVRAKLARI_HEADER))
        header = self.wait_clickable(self.BIRIM_EVRAKLARI_HEADER)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", header)
        header.click()

        submenu = self.wait_present(self.TESLIM_ALINMAYI_BEKLEYENLER_MENU)
        submenu.click()

        self.wait_visible(self.INBOX_TABLE)
        self.wait.until(lambda d: len(d.find_elements(*self.INBOX_ROWS)) > 0)

    # ========================= İMZA TARİHİ VE GEREĞİNİN KONTROLÜ =========================
    def check_signature_and_geregi(self, expected_time, expected_geregi):
        rows = self.driver.find_elements(*self.INBOX_ROWS)
        for row in rows:
            row_text = row.text
            if expected_time in row_text and expected_geregi in row_text:
                return True
        return False

    # ========================= LOG =========================
    def log_signature(self, imza_zamani, secilen_geregi):
        with open("signature_log.txt", "a", encoding="utf-8") as f:
            f.write(f"[IMZA] {imza_zamani} | GEREĞİ: {secilen_geregi}\n")
            f.flush()

    # ========================= TESLİM LİSTESİNDE EVRAK NO KONTROL ========================
    def check_evrak_no_in_teslim_list(self, timeout_seconds=60, interval_seconds=5):
        # 1️⃣ İmzaladıklarım tablosundan Evrak Numarasını al
        imzaladigim_divs = self.driver.find_elements(By.CSS_SELECTOR, "div.searchText")
        imzaladigim_text = next(
            (d.text.strip() for d in imzaladigim_divs if "No:" in d.text), None
        )
        if not imzaladigim_text:
            raise ValueError("İmzaladıklarım listesinde Evrak No bulunamadı.")

        # Regex ile Evrak Numarasını çek
        match = re.search(r"No:\s*([\d\-\.\w]+)", imzaladigim_text)
        if not match:
            raise ValueError(f"Evrak Numarası regex ile bulunamadı: '{imzaladigim_text}'")
        evrak_no = match.group(1).strip()
        print(f"İmzaladıklarım listesinden Evrak No: '{evrak_no}' alındı.")

        # 2️⃣ Teslim Alınmayı Bekleyenler listesine git
        self.go_to_teslim_alinmayi_bekleyenler()
        self._wait_table_ready()

        # 3️⃣ Polling ile tabloya düşmesini kısa süreli kontrol et
        start = time.time()
        found = False
        while time.time() - start < timeout_seconds:
            rows = self.driver.find_elements(By.XPATH, "//*[@id='mainInboxForm:inboxDataTable_data']/tr")
            for row in rows:
                try:
                    divs = row.find_elements(By.CSS_SELECTOR, "div.searchText")
                    for div in divs:
                        div_text = div.text.strip()
                        if evrak_no in div_text:
                            print(f"Eşleşen kayıt bulundu: Evrak No='{evrak_no}'")
                            found = True
                            break
                    if found:
                        break
                except:
                    continue
            if found:
                break
            time.sleep(interval_seconds)

        # 4️⃣ Bulunamazsa test fail
        if not found:
            raise AssertionError(f"Teslim Alınmayı Bekleyenler listesinde Evrak No='{evrak_no}' kısa sürede görünmedi.")

        return True
