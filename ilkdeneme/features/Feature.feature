Feature: Garanti BBVA web sayfası çeşitli testleri

  Scenario: Garanti BBVA Mevduat Ürünleri
      Given Garanti BBVA resmi web sayfası açılır
      When Mevduat'a tıklanır
      When Mevduat ürünlerinin bulunduğu sayfa açılır
      When Sayfa aşağıya kaydırılır
      When Daha Fazla Gör'e tıklanır
      When sayfadaki başlıklar kontrol edilir
      Then başlıklar hatasız olmalıdır


  Scenario: Garanti BBVA sitesinde arama yapma işlemi
    Given Garanti BBVA resmi web sayfası arama için açılır
    When Arama kutusuna basılır
    Then Arama kutusuna 'mevduat' yazılır ve Enter'a basılır
    Then Arama sonrası kaç sonuç bulundu


  Scenario: Garanti BBVA sitesinde olabilecek kırık görselleri tespit etme
    Given Garanti BBVA ana sayfası açılır
    When Görsel tespiti
    Then Kırık görsel bulunamadı


  Scenario: Garanti BBVA kredi-faiz oranını hesaplama
    Given Garanti BBVA web sayfası açılır
    When Sayfa kredi bölümüne kaydırılır
    When Kredi türlerine sırayla tıklanır ve değerler girilir
    Then Test tamamlandıktan sonra tarayıcı kapatılır