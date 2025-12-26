from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

import time, os

class LeftMenuPage(BasePage):

    
    # ========================= İMZALANAN EVRAKLAR =========================
    ISLEM_YAPTIKLARIM_HEADER = (By.XPATH, "//h3[text()='İşlem Yaptıklarım']")
    ISLEM_ALT_MENU = (By.XPATH, "//*[@id='esm_715431183_emi_1191786840']/span")
    

    def go_to_signed_documents(self):
        self.js_click(self.wait_clickable(self.ISLEM_YAPTIKLARIM_HEADER))
        self.js_click(self.wait_visible(self.ISLEM_ALT_MENU))
  