# Çalışma Soruları

## Çalışma 1
Aşağıdaki gereksinime ait test senaryolarını Gherkin dilinde yazınız, dilediğiniz formatta teslimat yapabilirsiniz.

**Gereksinim:** Kullanıcı, çizgi çizim aracı ile gradyan ve derece birimlerinde açı ölçme işlemi yapabilmelidir.

**Gereksinim detayı:**

# Açı Ölç İşlemi Gereksinim Tablosu

| Başlık            | Açıklama                                                                 |
|-------------------|---------------------------------------------------------------------------|
| Açı Ölç İşlemi    | Harita ekranı üzerinde herhangi koordinatta üç nokta seçilerek açı ölçme işlemi yapılır. Açı değeri harita ekranında görüntülenir. |
| Çizgi Görünümü    | İşlem gerçekleşirken açıyı oluşturan kırık noktaları arasındaki çizgi harita ekranında izlenebilir. |
| Çıkış             | İşlem seçiminden ''Açı Ölç'' butonunun tekrar seçilmesi ile çıkılır. |
| İmleç             | İşlemin seçilmesi ile birlikte imleç “+”(crosshair) şeklinde görüntülenir. |
| Nokta Seçimi      | Ölçü elde edebilmek için harita ekranında üç noktanın gösterilmesi gerekir. |
| Çizgi Nesnesi     | Noktaların gösterilmesi ile noktalar arasında çizgi nesnesi oluşturulur. |
| İçerik Balonu     | Üçüncü noktanın seçilmesi ile grad ve derece birimlerinde gösterilmek üzere içerik balonu içerisinde gelir. (1 grad 9/10 dereceye eşittir.) |
| Yeni Ölçüm        | Yeni bir açı ölçme işlemine başlandığında bir önceki açıyı oluşturan çizgiler ve içerik balonu kaybolur. |

---

# Açı Bilgisi Gereksinim Tablosu

| Başlık                  | Açıklama                                                                 |
|--------------------------|---------------------------------------------------------------------------|
| Açı Gösterimi (Balon)    | Açı ölçüsünün yer aldığı alandır, değer noktaların işaretlenmesi ile otomatik yansır. |
| Başlangıç Değeri         | Nokta gösterimine başlanır başlanmaz harita ekranında belirir, üçüncü nokta gösterilene kadar değerler 0.00 olarak yer alır. |
| Format                   | Ölçü değeri ondalık sayı olarak, noktadan sonra 2 basamak gösterilmektedir. |
| Birimler                 | Ölçü değerleri grad ve derece cinsinden gösterilir, sembolleri ölçü değeri ile birlikte baloncukta yer alır. |

---

# Açı Editleme İşlemi Gereksinim Tablosu

| Başlık                  | Açıklama                                                                 |
|--------------------------|---------------------------------------------------------------------------|
| Geometri Değişikliği     | Açı ölç işlemi ile çizilmiş çizginin geometrisi köşe veya kırık noktaları sürüklenerek, silinerek değişiklik yapılabilir. |
| Nokta Renklenmesi        | Çizgi şekli köşe noktaların üzerine gelindiğinde noktalar farklı bir renk ile renklenir. |
| Dinamik Değer            | Mouse ile tutulup sürüklenmesi yöntemi ile açı değerinin dinamik değişiklik gösterdiği gözlemlenir. |
| Nokta Silme              | Köşe noktanın art arda iki kez gösterilmesi ile nokta silinir ve açı değerinin 0.00 hesaplandığı içerik balonunda görülür. |

# Çalışma Soruları

## Çalışma 2
Bir kayıt işlemi için aşağıdaki çözüm dokümanı oluşturulmuştur, test adımlarının netliği açısından eksik/çelişkili gördüğünüz noktaları belirtiniz, dilediğiniz formatta teslimat yapabilirsiniz.

# Kayıt İşlemi Gereksinim Tablosu

| Bileşen Adı              | Açıklama                                                                 | Kısıtlar                                               | Veri Tipi    |
|---------------------------|--------------------------------------------------------------------------|--------------------------------------------------------|--------------|
| Tanıtım No                | T.C.Kimlik no/Yabancı Kimlik No/Vergi No/Mersis No/Pasaport No girilir. | Mak. 20 hane                                           | Alfanumerik  |
| Adı Soyadı/Unvanı         | Adı soyadı/unvanı girilir.                                               | En az 2 karakter girilmelidir. Girilmediğinde sistem tarafından "En az iki haneli olacak şekilde giriniz." şeklinde uyarı mesajı verilir. | Text         |
| Baba Adı                  | Baba adı girilir.                                                       |                                                        | Text         |
| Başlangıç Kayıt Tarihi    | Başlangıç kayıt tarihi seçimi yapılır.                                   |                                                        | Date         |
| Bitiş Kayıt Tarihi        | Bitiş kayıt tarihi seçimi yapılır.                                       |                                                        | Date         |
| Kaydı Yapan Kurum         | Kaydı yapan kurum seçilir.                                               | Sayfa ilk açıldığında Müdürlük Kayıtları seçili olarak görüntülenir. Kullanıcı tarafından değiştirilebilir. | Combobox     |
| Bölge                     |                        |                                                        | Combobox     |
| İl                        |          | Birden fazla il seçilebilir ya da il seçilmeden devam edilebilir. | Combobox     |
| İlgili Müdürlük/Müdürlükler| Birden fazla müdürlük seçilebilir.                                      | Bölge ya da il seçimi yapılmadan Müdürlük seçilemez. En az biri seçilmeli. Bölge/İl seçimine bağlı olan müdürlükler görüntülenir. Müdürlük seçilmeden kayıt işlemi gerçekleştirilemez. | Combobox     |
| Durumu                    | Kaydın durumunun seçimi yapılır.                                        | Aktif ve Pasif seçenekleri görüntülenir. Sayfa ilk açıldığında Aktif seçeneği seçili olarak görüntülenir. Kullanıcı tarafından değiştirilebilir. Tümü, Aktif, Pasif seçenekleri gelir. | Tümü    |
| Kaydet                    |                                               |                                                        | Buton        |


## Çalışma 3
Belgenet projesinde Tek imzacılı resmi yazı oluşturulması senaryosu genel olarak aşağıdaki şekildedir, tercih ettiğiniz herhangi bir dil/tool ile otomasyonunu gerçekleştiriniz.

**Link:** https://www.belgenet.com.tr/  
**Kullanıcı Adı:** botcu  
**Password:** spider  

### Evrak oluşturmanın genel işleyişi
- Üst menü > evrak oluştur menüsünü aç  
- Editör ve bilgilerinde zorunlu alanları doldur  
- Gereği alanında işlem yapılan birimi seç  
- İmza alanından güncel kullanıcıyı imzacı olarak seç ve **Kullan** butonunu tıkla  
- Ekler tabından dosya ekle  
- Sağ üst köşede **İmzala** butonunu tıkla  
- Gelen pop upta **s-imza** seç, imzala  
- Sol menü > **İşlem Yaptıklarım > İmzaladıklarım** listesine evrakın düştüğünü gör  
- Sol menü > **Birim Evrakları > Teslim alınmayı bekleyenler** listesine evrakın düştüğünü gör  


## Çalışma 4 
Çalışma 3’te bulunan link üzerinde çeşitli senaryolar deneyerek, karşılaştığınız bir ya da daha fazla hatayı, bir defectte olması gereken kurallara uygun olacak şekilde raporlayınız.