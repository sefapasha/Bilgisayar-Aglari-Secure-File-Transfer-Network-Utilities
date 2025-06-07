## 📌 Projeye Genel Bakış

Bu proje, Python tabanlı temel bir dosya transfer sistemi ve ağ performans ölçüm araçlarını içermektedir.  
AES ve RSA tabanlı güçlü şifreleme mekanizmalarıyla güvenlik sağlanırken, paket parçalama, yeniden birleştirme ve IP başlık işlemleri gibi düşük seviyeli ağ işlemleri de ele alınmıştır.  
Ayrıca, Scapy ve diğer kütüphanelerle IP paketleri üzerinde TTL ve checksum gibi alanlar manipüle edilmiştir.

---

## ⚙️ Özellikler ve Teknik Detaylar

### Dosya Transfer Sistemi
- RSA tabanlı anahtar değişimi ile AES şifreleme anahtarı güvenli olarak paylaşılır.
- Dosya AES ile şifrelenir, SHA-256 ile bütünlük doğrulaması yapılır.
- Manuel olarak veri paketlere bölünür (fragmentation) ve alıcıda yeniden birleştirilir (reassembly).

### Güvenlik Mekanizmaları
- AES tabanlı şifreleme uygulanmıştır
- SHA-256 hash ile dosya bütünlüğü sağlanır.

### Düşük Seviyeli IP İşlemleri
- Scapy ve socket kütüphaneleri ile IP paketleri oluşturulup, TTL ve checksum alanları manuel olarak ayarlanabilir.
- IP paketlerinin el ile oluşturulması ve gönderilmesi sağlanır.

### Ağ Performans Ölçümü
- `ping` komutuyla gecikme (latency) ölçümü.
- iPerf3 ile bant genişliği testleri (gerektiğinde aktif hale getirilebilir).

---
## 🚀 Nasıl Çalıştırılır?
1. Sunucu tarafı çalıştırılır: python server.py
2. İstemci tarafı çalıştırılır: python client.py
3. Dosya received_file.txt olarak sunucuya kaydedilir ve bütünlük doğrulaması yapılır.
4. performance.py ile gecikme süresi ölçülür.
5. ip_utils.py veya scapy_packet.py ile IP paketleri üzerinde TTL ve checksum işlemleri denenebilir.

## 📌 Gereksinimler
Python 3.8+
PyCryptodome
Scapy
iPerf3 (isteğe bağlı, sadece bant genişliği testi için)
Wireshark

Kurulum için:
pip install pycryptodome scapy

## 📁 Dosya Yapısı

```
.
├── client.py            # Dosya gönderen istemci kodu
├── server.py            # Dosya alan sunucu kodu
├── encryption.py        # RSA ve AES şifreleme, hash fonksiyonları
├── fragmenter.py        # Veri parçalama ve yeniden birleştirme fonksiyonları
├── ip_utils.py          # IP header oluşturma, checksum hesaplama, paket gönderme
├── perfomance.py        # Ping gecikme ölçümü
└── file_to_send.txt     # Gönderilecek örnek dosya

## 📺 Youtube Video Linki
https://youtu.be/-s8U8dugE5Y
