Feature: Açı Ölçme ve Editleme İşlemleri
  Kullanıcı harita ekranında üç nokta seçerek açı ölçme işlemi yapabilmeli.
  Ölçüm grad ve derece birimlerinde içerik balonunda gösterilmeli.
  Çizgi editleme işlemleri yapılabilmelidir.

  Background:
    Given Kullanıcı harita ekranını açmıştır
    And Kullanıcı "Açı Ölç" butonuna tıklamıştır
    Then İmleç crosshair (“+”) şeklinde görünmelidir

  Scenario: Üç nokta seçilerek açı ölçülmesi
    Given Kullanıcı harita ekranında üç nokta seçer
    When Noktalar arasında çizgi nesnesi oluşturulur
    Then Üçüncü nokta seçildiğinde içerik balonu görünmelidir
    And İçerik balonunda açı değeri grad ve derece birimlerinde gösterilmelidir

  Scenario: Başlangıçta 0.00 değerlerinin gösterilmesi
    Given Kullanıcı açı ölçümüne başlar
    When Henüz üçüncü nokta seçilmemiştir
    Then İçerik balonunda değerler 0.00 olarak görünmelidir

  Scenario: Ölçüm değerlerinin formatı
    Given Kullanıcı üç nokta seçerek açı ölçümü yapar
    Then İçerik balonunda ölçüm değeri iki ondalık basamakla gösterilmelidir
    And Ölçüm değeri yanında grad ve derece sembolleri yer almalıdır

  Scenario: Yeni ölçüm başlatıldığında önceki ölçümün kaybolması
    Given Kullanıcı üç nokta seçerek açı ölçümü yapmıştır
    When Kullanıcı yeni bir açı ölçümüne başlar
    Then Önceki çizgiler ve içerik balonu kaybolmalıdır

  Scenario: Açı ölçümünden çıkış
    Given Kullanıcı açı ölçümüne başlamıştır
    When Kullanıcı "Açı Ölç" butonuna tekrar tıklar
    Then Açı ölçüm işlemi sonlanmalıdır
    And İmleç normal hale dönmelidir

  Scenario: Köşe noktalarının sürüklenmesi ile açı değerinin değişmesi
    Given Kullanıcı açı ölçümü yapmıştır
    When Kullanıcı köşe noktasını mouse ile sürükler
    Then Çizgi geometrisi değişmelidir
    And İçerik balonundaki açı değeri dinamik olarak güncellenmelidir

  Scenario: Köşe noktasının silinmesi
    Given Kullanıcı açı ölçümü yapmıştır
    When Kullanıcı aynı köşe noktasını art arda iki kez seçer
    Then Nokta silinmelidir
    And İçerik balonunda açı değeri 0.00 olarak görünmelidir

  Scenario: Köşe noktasının üzerine gelindiğinde renk değişimi
    Given Kullanıcı açı ölçümü yapmıştır
    When Kullanıcı köşe noktasının üzerine gelir
    Then Nokta farklı bir renkle vurgulanmalıdır
