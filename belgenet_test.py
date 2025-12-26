from selenium import webdriver
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException



driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 20)

# 1. Siteye git
driver.get("https://www.belgenet.com.tr/")

# 2. Demo seçimi
wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//*[@id='menu']/ul/li[1]/a"))
).click()

# 3. Login
wait.until(EC.visibility_of_element_located(
    (By.ID, "parolaSertifikaAccordion:uForm:txtUKullaniciAdi"))
).send_keys("botcu")

driver.find_element(By.ID, "loginUSifre").send_keys("spider")

wait.until(EC.element_to_be_clickable(
    (By.ID, "parolaSertifikaAccordion:uForm:girisYapButton"))
).click()

# 4. Evrak oluştur menüsü
wait.until(EC.element_to_be_clickable(
    (By.ID, "topMenuForm2:ust:0:ustMenuEleman"))
).click()

wait.until(EC.element_to_be_clickable(
    (By.LINK_TEXT, "Evrak Oluştur"))
).click()

# 5. Klasör seçimi
wait.until(EC.element_to_be_clickable(
    (By.ID, "yeniGidenEvrakForm:evrakBilgileriList:4:eklenecekKlasorlerLov:treeButton"))
).click()

wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//*[@id='yeniGidenEvrakForm:evrakBilgileriList:4:eklenecekKlasorlerLov:lovTree:0']/span/span[1]"))
).click()

wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//*[@id='yeniGidenEvrakForm:evrakBilgileriList:4:eklenecekKlasorlerLov:lovTree:0_0']/span/span[3]"))
).click()

wait.until(EC.element_to_be_clickable(
    (By.ID, "yeniGidenEvrakForm:evrakBilgileriList:4:eklenecekKlasorlerLov:lovOverlayPanelKapat"))
).click()

# 6. Gereği seçimi
wait.until(EC.element_to_be_clickable(
    (By.ID, "yeniGidenEvrakForm:evrakBilgileriList:20:geregiLov:treeButton"))
).click()
time.sleep(5)
# Önce ana div'in yüklenmesini bekle 
wait.until( EC.presence_of_element_located((By.ID, "yeniGidenEvrakForm:evrakBilgileriList:20:geregiLov:lovTree:0")) ) 

target_element = wait.until( EC.element_to_be_clickable((By.XPATH, "//*[@id='yeniGidenEvrakForm:evrakBilgileriList:20:geregiLov:lovTree:0']/span/span[1]")) ) 
target_element.click()
time.sleep(5)

# Sonra içindeki span/span[1] elementini bekle ve tıkla 
target_element = wait.until( EC.element_to_be_clickable((By.ID, "yeniGidenEvrakForm:evrakBilgileriList:20:geregiLov:lovTree:0_59")) ) 
target_element.click()
time.sleep(5)

wait.until(EC.element_to_be_clickable(
    (By.ID, "yeniGidenEvrakForm:evrakBilgileriList:20:geregiLov:lovOverlayPanelKapat"))
).click()

# 7. Onay akışı
# "Otomatik Onay Akışı Ekle" butonunu bekle ve tıkla
otomatik_onay_btn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//*[contains(@id,'otomatikOnayAkisiEkle')]"))
)
otomatik_onay_btn.click()

# "Hiyerarşik Akış Oluştur" dialog pencereyi bekle
wait.until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(@id,'hiyerarsikAkisOlusturDialog')]"))
)

# Checkbox’ı bekle ve tıkla
checkbox = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//*[contains(@id,'otomatikAkisKullaniciBirimListId_null_checkbox')]"))
)
checkbox.click()

# Dropdown'u bul
dropdown_xpath = "//*[@id='yeniGidenEvrakForm:hiyerarsikAkisOlusturForm:otomatikAkisKullaniciBirimListId_data']/tr[1]/td[6]/select"

# Option[4] (index 3) seç
option_xpath = dropdown_xpath + "/option[4]"
option = wait.until(EC.element_to_be_clickable((By.XPATH, option_xpath)))
option.click()

# Seçilen option'un metninde 'imzalama' yazmasını bekle
selected_option_xpath = dropdown_xpath + "/option[@selected='selected']"
wait.until(EC.text_to_be_present_in_element((By.XPATH, selected_option_xpath), "İmzalama"))

# "Hiyerarşik Akış Kullan" butonunu bekle ve tıkla
submit_btn_xpath = "//*[contains(@id,'hiyerarsikAkisKullan')]"
submit_btn = wait.until(EC.element_to_be_clickable((By.XPATH, submit_btn_xpath)))
submit_btn.click()

# Editör butonunu bekle ve tıkla
cmdbutton = driver.find_element(By.ID, "yeniGidenEvrakForm:leftTab:uiRepeat:1:cmdbutton")
driver.execute_script("arguments[0].click();", cmdbutton)

input_editor = wait.until(
    EC.element_to_be_clickable((By.ID, "yeniGidenEvrakForm:hitapUstVeriEkle"))
)
input_editor.click()

input_editor = wait.until(
    EC.element_to_be_clickable((By.ID, "yeniGidenEvrakForm:hitapEkInplaceTextId"))
)
input_editor.send_keys("XYZ")


wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//*[@id='yeniGidenEvrakForm:j_idt10762']"))
).click()
time.sleep(5)


# CKEditor iframe'ine geç
iframe = WebDriverWait(driver, 10).until(
    EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//*[@id='cke_2_contents']/iframe"))
)

# iframe içindeki body'yi bul ve yazı ekle
ckeditor_body = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "body"))
)
ckeditor_body.clear()
ckeditor_body.send_keys("Test Evrak içeriği buraya yazıldı")

# tekrar ana sayfaya dön
driver.switch_to.default_content()


# Alan görünür olana kadar bekle 
imzaci_input = wait.until( EC.visibility_of_element_located((By.ID, "yeniGidenEvrakForm:imzacilarPanelUiId:0:imzacilarPanelUiRepeatId:2:ImzacıUstVeriEkle")) ) 
imzaci_input.click()


# Önce pencerenin görünür olmasını bekle
dialog = wait.until(
    EC.visibility_of_element_located((By.ID, "yeniGidenEvrakForm:imzacilarPanelUiId:0:imzacilarPanelUiRepeatId:2:imzaciAdinaInplaceDialogOutputPanelID"))
)

# Sonra pencere içindeki input alanını bul
input_field = wait.until(
    EC.visibility_of_element_located((By.ID, "yeniGidenEvrakForm:imzacilarPanelUiId:0:imzacilarPanelUiRepeatId:2:j_idt10798"))
)

# Metin yaz
input_field.clear()
input_field.send_keys("Deneme İmza Metni")

wait.until(EC.element_to_be_clickable(
    (By.ID, "yeniGidenEvrakForm:imzacilarPanelUiId:0:imzacilarPanelUiRepeatId:2:imzaciAdinaInplaceTamamButonID"))
).click()


# Ekler butonunu bekle ve tıkla
cmdbutton = driver.find_element(By.ID, "yeniGidenEvrakForm:leftTab:uiRepeat:2:panelGrid")
driver.execute_script("arguments[0].click();", cmdbutton)

input_editor = wait.until(
    EC.element_to_be_clickable((By.ID, "yeniGidenEvrakForm:leftTab:uiRepeat:2:cmdbutton"))
)
input_editor.click()


# Textarea görünür olana kadar bekle
textarea = wait.until(
    EC.visibility_of_element_located((By.ID, "yeniGidenEvrakForm:evrakEkTabView:dosyaAciklama"))
)

# İçeriği temizle ve metin yaz
textarea.clear()
textarea.send_keys("Bu evrak için ek açıklama metni girildi.")

wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//*[@id='yeniGidenEvrakForm:evrakEkTabView:fileUploadButtonA']/div[1]/span"))
).click()


#-------Dosya yükleme penceresi
time.sleep(2)  # modalın açılmasını bekle
pyautogui.write(r"C:\Users\MSI\Downloads\file-sample_100kB.doc")
pyautogui.press("enter")  # dosyayı seç ve modalı kapat
#-------

# Dosya ekle butonuna tıkla
dosya_ekle_btn = wait.until(
    EC.element_to_be_clickable((By.ID, "yeniGidenEvrakForm:evrakEkTabView:dosyaEkleButton"))
)
dosya_ekle_btn.click()
print("Dosya başarıyla yüklendi.")

# İmzala butonunu bekle ve tıkla 
button = wait.until( EC.element_to_be_clickable((By.ID, "yeniGidenEvrakForm:rightTab:uiRepeat:2:cmdbutton")) ) 
button.click()

try:
    # Önce dialogun görünür olmasını bekle
    dialog = wait.until(
        EC.visibility_of_element_located((By.ID, "evrakImzalaDialog"))
    )
    print("evrakImzalaDialog açıldı.")

    # Dialog içindeki 'İmzala' butonunu bekle
    confirm_btn = wait.until(
        EC.element_to_be_clickable((By.ID, "imzalaForm:sayisalImzaConfirmDialogOpener"))
    )

    # Bazı UI frameworklerinde normal click çalışmaz, JS ile tıklamak daha güvenli
    driver.execute_script("arguments[0].click();", confirm_btn)
    print("Sayısal imza onay butonuna tıklandı.")

except TimeoutException:
    print("Dialog veya buton bulunamadı.")

sayisal_imzala_btn = wait.until(
    EC.element_to_be_clickable((By.ID, "imzalaForm:sayisalImzaConfirmForm:sayisalImzaEvetButton"))
)
sayisal_imzala_btn.click()

time.sleep(5)


try:
    # 1. Üst başlığı bul ve JS ile tıkla
    header = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//h3[text()='İşlem Yaptıklarım']"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", header)
    driver.execute_script("arguments[0].click();", header)
    print("Üst başlığa tıklandı.")

    # 2. Alt başlık görünür olana kadar bekle
    sub_item = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='esm_715431183_emi_1191786840']/span"))
    )
    print("Alt başlık göründü.")

    # 3. Alt başlığa tıkla
    driver.execute_script("arguments[0].click();", sub_item)
    print("Alt başlığa tıklandı.")

except TimeoutException:
    print("Üst başlık veya alt başlık bulunamadı.")



time.sleep(5)

# 9. Evrak bilgileri
# wait.until(EC.visibility_of_element_located((By.ID, "title"))).send_keys("Test Evrak")
# wait.until(EC.visibility_of_element_located((By.ID, "description"))).send_keys("Otomasyon ile oluşturuldu")

# 10. Çıkış
driver.quit()
