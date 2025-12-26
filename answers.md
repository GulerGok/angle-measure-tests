# Çalışma 1- Angle Measurement Feature

Bu proje, verilen gereksinimlere uygun olarak Gherkin dilinde hazırlanmış test senaryolarını içerir.  

## İçerik
- `features/AngleMeasurement.feature`: Gereksinimlere uygun senaryolar
- `steps/angleSteps.js`: Dosya oluşturulmuş ancak içi boş bırakılmıştır. Step definition’lar uygulamanın HTML/CSS yapısına göre uyarlanmalıdır.
- `README.md`: Açıklama ve kullanım notları

## Not
- Senaryolar Playwright + Cucumber entegrasyonu için kullanılabilir.
- Step definition’lar uygulamanın HTML/CSS yapısına göre uyarlanmalıdır.
- Gereksinim dokümanında bu detaylar verilmediği için dosya yalnızca Gherkin senaryolarını içermektedir.



# Çalışma 2 - Kayıt İşlemi Çözüm Dokümanı İncelemesi

Bu rapor, verilen kayıt işlemi çözüm dokümanındaki eksik ve çelişkili noktaları test adımlarının netliği açısından değerlendirmek amacıyla hazırlanmıştır.

---

## 📋 Eksik / Çelişkili Noktalar Tablosu

| Bileşen | Eksik / Çelişkili Nokta | Açıklama / Teste Etkisi |
|---------|--------------------------|--------------------------|
| **Tanıtım No** | Minimum karakter sınırı belirtilmemiş | Maksimum 20 hane var ama minimum kaç hane girilmeli net değil. |
| **Adı Soyadı/Unvanı** | Maksimum uzunluk belirtilmemiş | Çok uzun girişlerde sistem davranışı belirsiz. |
| **Baba Adı** | Kısıtlar belirtilmemiş | Boş bırakılabilir mi, minimum/maximum uzunluk var mı? |
| **Başlangıç / Bitiş Kayıt Tarihi** | Tarih aralığı kuralı yok | Bitiş tarihi başlangıçtan önce seçilirse ne olacak? Validasyon eksik. |
| **Kaydı Yapan Kurum** | Seçenekler belirsiz | Müdürlük Kayıtları dışında hangi kurumlar listeleniyor, sınırlandırma yok. |
| **Bölge** | Zorunluluk durumu belirtilmemiş | Birden fazla seçilebilir denmiş ama hiç seçilmeden devam edilebilir mi? |
| **İl** | Çelişki var | “İl seçilmeden devam edilebilir” deniyor, ancak müdürlük seçimi için bölge/il zorunlu. |
| **İlgili Müdürlük/Müdürlükler** | Zorunluluk kuralı net değil | “En az biri seçilmeli” deniyor. İl seçilmeden devam edilebilir ifadesiyle çelişiyor. |
| **Durumu** | Veri Tipi yanlış, varsayılan değer çelişkili | Veri Tipi kısmında “Tümü” yazıyor, aslında Combobox olmalı. Seçenekler “Tümü, Aktif, Pasif” denmiş ama ilk değer hem “Aktif” hem “Tümü” olarak belirtilmiş. Netleştirilmesi gerekiyor. |
| **Kaydet Butonu** | Validasyon sonrası davranış belirtilmemiş | Eksik/yanlış veri girildiğinde kayıt butonuna basılırsa ne olacak? Hata mesajı mı, kayıt engellenmesi mi? |

---

## 📑 Özet

- **Eksik kurallar:** Minimum değerler, maksimum uzunluklar, tarih aralığı validasyonu.  
- **Çelişkiler:** İl seçimi opsiyonel mi değil mi, Müdürlük seçimi zorunluluğu, Durum alanında varsayılan değer.  
- **Belirsizlikler:** Baba adı zorunlu mu, Kaydet butonunun hata senaryolarındaki davranışı.  

Bu noktalar netleştirilmeden test senaryoları tam olarak yazılamaz.

---

## 📝 Örnek Gherkin Senaryoları

```gherkin
Scenario: Bitiş tarihi başlangıçtan önce seçildiğinde uyarı verilmesi
  Given Kullanıcı başlangıç tarihini 01.01.2025 seçer
  And Kullanıcı bitiş tarihini 31.12.2024 seçer
  When Kullanıcı Kaydet butonuna tıklar
  Then Sistem "Bitiş tarihi başlangıç tarihinden önce olamaz." uyarısı vermelidir

Scenario: Durum alanında varsayılan değer kontrolü
  Given Kullanıcı kayıt ekranını açar
  Then Durum alanında varsayılan olarak "Tümü" seçili olmalıdır
  And Kullanıcı "Aktif" veya "Pasif" seçeneklerini seçebilir
```

# Çalışma 3 - Otomasyon Çalışması
Belgenet projesinde Tek imzacılı resmi yazı oluşturulması senaryosunun otomasyonu Python + Selenium ile gerçekleştirilmiştir. (python -m tests.test_evrak komutu ile çalıştırabilirsiniz)