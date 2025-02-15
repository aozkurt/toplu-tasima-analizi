# Kırklareli Toplu Taşıma Planlama

Bu proje, Kırklareli'ndeki üç mahalle için en uygun toplu taşıma güzergahını belirlemek amacıyla geliştirilmiştir.
Softmax algoritması kullanılarak en uygun güzergah seçilir.

---

### **Örnek Çıktı**
```
Kriter Ağırlıkları: [0.05301026 0.39169577 0.39169577 0.01950138 0.14409682]
```
```
En iyi rota: İstasyon Mahallesi
```
```
Tüm rotalar:
```
```
Cumhuriyet Mahallesi = 0.644845
```
```
İstasyon Mahallesi = 0.766423
```
```
Pınar Mahallesi = 0.680539
```
## Kurulum

Aşağıdaki adımları takip ederek projeyi çalıştırabilirsiniz:

Depoyu klonlayın:
```bash
git clone https://github.com/aozkurt/toplu-tasima-analizi.git
```
```md
## Kullanım

Aşağıdaki komutu çalıştırarak en uygun güzergahı hesaplayabilirsiniz:

```bash
python main.py
```

### **Proje Mimarisi ve Açıklamalar**
- Softmax metodu kullanıldı.
