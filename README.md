# takip-etmeyenleri-bulma-scripti

Bu Python scripti, Instagram'da takip ettiğiniz kişileri ve sizi takip eden kişileri karşılaştırarak sizi takip etmeyen kişileri bulmanızı sağlar.

Script, iki HTML dosyasını okur:

following.html - takip ettiğiniz hesapları içerir.
followers.html - sizi takip eden hesapları içerir.
Bu HTML dosyaları, BeautifulSoup kütüphanesi kullanılarak parse edilir ve hesap isimleri çıkarılır. Script, bu iki liste arasındaki farkı hesaplar ve takip ettiğiniz fakat sizi takip etmeyen hesapları bulur.

Nasıl Çalışır?
Script, following.html ve followers_1.html dosyalarının içeriğini okur.
Bu HTML dosyaları BeautifulSoup kullanılarak parse edilir ve hesap isimleri çıkarılır.
Takip ettiğiniz hesapların isimleri following_names listesine, sizi takip eden hesapların isimleri ise followers_names listesine kaydedilir.
Python'ın set işlemleri kullanılarak following_names ile followers_names arasındaki fark hesaplanır.
Son olarak, sizi takip etmeyen hesapların isimleri ekrana yazdırılır.

Gerekli Ön Koşullar
Python 3.x
BeautifulSoup 4 kütüphanesi
Takipçi ve takip edilen listelerini içeren HTML dosyaları
Gerekli kütüphaneleri pip kullanarak yükleyebilirsiniz:
pip install beautifulsoup4

Kullanım
Instagram hesabınızdan takipçi ve takip edilen listelerinizi indirin. Bunun için Instagram'dan Veri İndirme talebi oluşturarak verilerinizi alabilirsiniz. İndirilen veri paketinden followers.html ve following.html dosyalarını çıkarın.
Bu dosyaları script ile aynı dizine yerleştirin.

Scripti Python ile çalıştırın:
python takip_edenleri_bul.py
Script, sizi takip etmeyen hesapların isimlerini ekrana yazdıracaktır.
