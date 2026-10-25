# 🚀 Railway Deployment - Adım Adım Rehber

## ✅ Ön Gereksinimler

1. **GitHub Hesabı** (zaten var)
2. **Railway Hesabı** - https://railway.app (GitHub ile giriş)
3. **Repository** - Blackbird dosyalarını GitHub'a push et

---

## 📦 1. GitHub'a Push Et

```bash
# Repository'yi başlat
cd blackbird-main
git init

# Tüm dosyaları ekle
git add .

# Commit yap
git commit -m "Add Blackbird API for Railway deployment"

# GitHub'da yeni repo oluştur ve bağlan
git remote add origin https://github.com/YOUR_USERNAME/blackbird-api.git
git branch -M main
git push -u origin main
```

**ÖNEMLİ:** `.env` dosyası `.gitignore`'da olduğu için push edilmeyecek (güvenlik için doğru)

---

## 🛤️ 2. Railway'de Proje Oluştur

### Adım 1: Railway'e Git
1. https://railway.app adresine git
2. **"Start a New Project"** butonuna tık
3. **"Deploy from GitHub repo"** seçeneğini seç

### Adım 2: Repository Seç
1. GitHub hesabınızı bağlayın (ilk defaysa)
2. **blackbird-api** repository'nizi seçin
3. **"Deploy Now"** butonuna tıklayın

### Adım 3: Railway Otomatik Deploy Başlattı
Railway şunları otomatik yapacak:
- ✅ `Dockerfile.api` dosyasını bulacak
- ✅ Docker image'ı build edecek
- ✅ Container'ı başlatacak
- ✅ Public URL verecek

---

## ⚙️ 3. Environment Variables Ayarla

### Railway Dashboard'da:

1. Projenize tıklayın
2. **"Variables"** sekmesine gidin
3. **"Add Variable"** butonuna tıklayın

### Eklenecek Değişkenler:

```env
# ZORUNLU
PORT=8000

# OPSIYONEL (Instagram aramaları için)
INSTAGRAM_SESSION_ID=your_instagram_session_id_here

# OPSIYONEL (AI özellikleri için)
# Şimdilik boş bırakabilirsin, sonra eklersin
```

**SADECE PORT=8000 YETERLI!** Diğerleri opsiyonel.

---

## 🔍 4. Deploy İzleme

### Build Logs'u İzle:

Railway Dashboard'da:
1. **"Deployments"** sekmesine git
2. En son deployment'a tıkla
3. **"View Logs"** butonuna tıkla

### Beklenen Log Çıktısı:
```
Building with Dockerfile.api...
Step 1/5 : FROM python:3.12-slim
Step 2/5 : WORKDIR /app
Step 3/5 : COPY . .
Step 4/5 : RUN pip install...
Step 5/5 : CMD ["python", "api.py"]
Build successful!
Deploying...
INFO:     Started server process
INFO:     Uvicorn running on http://0.0.0.0:8000
```

✅ **"Uvicorn running"** gördüysen başarılı!

---

## 🌐 5. Public URL Al

### Railway Dashboard'da:

1. **"Settings"** sekmesine git
2. **"Networking"** bölümünü bul
3. **"Generate Domain"** butonuna tıkla
4. Railway sana otomatik bir URL verecek:
   ```
   https://blackbird-production.railway.app
   ```
   veya
   ```
   https://blackbird-production-xxxx.up.railway.app
   ```

**Bu URL'i not al!** API'n artık bu adreste çalışıyor.

---

## ✅ 6. Test Et

### Health Check:
```bash
curl https://your-app.railway.app/
```

**Beklenen Response:**
```json
{
  "status": "healthy",
  "version": "1.0.0",
  "sites_count": 600
}
```

### API Docs:
Tarayıcıda aç:
```
https://your-app.railway.app/docs
```

Interactive API dokümantasyonu göreceksin!

### Username Search Test:
```bash
curl -X POST https://your-app.railway.app/search/username \
  -H "Content-Type: application/json" \
  -d '{"username": "test", "no_nsfw": true}'
```

---

## 📊 Railway Dashboard Özellikleri

### 1. Deployments
- Build history
- Logs görüntüleme
- Rollback (eski versiyona dön)

### 2. Metrics
- CPU kullanımı
- Memory kullanımı
- Network traffic
- Response times

### 3. Variables
- Environment variables yönetimi
- Restart olmadan güncelleme

### 4. Settings
- Domain management
- Restart policy
- Resource allocation

---

## 🔄 Güncellemeler

### Kod Güncelledikten Sonra:

```bash
# Değişiklikleri commit et
git add .
git commit -m "Update API"

# GitHub'a push et
git push

# Railway otomatik olarak yeni deploy başlatır!
```

Railway her push'ta otomatik deploy yapar. Manuel bir şey yapman gerekmiyor!

---

## 💰 Maliyet

### Free Tier (Starter Plan):
- ✅ **$5/ay** ücretsiz kredi
- ✅ **500 saat** execution time/ay
- ✅ **8 GB RAM**
- ✅ **100 GB** outbound bandwidth
- ✅ **Unlimited** inbound bandwidth

**Blackbird API için fazlasıyla yeterli!**

Aylık kullanım:
- 24/7 çalışırsa: ~720 saat
- Free tier: 500 saat
- **İlk 500 saat ücretsiz**, sonrası ~$0.10/saat

---

## 🐛 Sorun Giderme

### Problem 1: Build Failed
```
Error: requirements-api.txt not found
```
**Çözüm:** Dosyanın repo'da olduğundan emin ol
```bash
git add requirements-api.txt
git commit -m "Add requirements"
git push
```

### Problem 2: Port Binding Error
```
Error: Address already in use
```
**Çözüm:** Railway Variables'da `PORT=8000` olduğundan emin ol

### Problem 3: Health Check Timeout
```
Error: Application failed to respond
```
**Çözüm:** 
1. Logs'u kontrol et
2. `api.py` dosyasının doğru olduğundan emin ol
3. Railway'i restart et

### Problem 4: 502 Bad Gateway
```
502 Bad Gateway
```
**Çözüm:** Deploy henüz bitmemiş olabilir. 2-3 dakika bekle.

---

## 📱 API Kullanımı

### Python'dan:
```python
import requests

API_URL = "https://your-app.railway.app"

response = requests.post(
    f"{API_URL}/search/username",
    json={"username": "johndoe", "no_nsfw": True}
)

data = response.json()
print(f"Bulundu: {data['total_found']} hesap")
```

### JavaScript'ten:
```javascript
const API_URL = "https://your-app.railway.app";

const response = await fetch(`${API_URL}/search/username`, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ username: 'johndoe', no_nsfw: true })
});

const data = await response.json();
console.log(`Bulundu: ${data.total_found} hesap`);
```

### cURL:
```bash
curl -X POST https://your-app.railway.app/search/username \
  -H "Content-Type: application/json" \
  -d '{"username": "johndoe"}'
```

---

## 🎯 Özet: Ne Yapman Gerekiyor?

### 1. GitHub'a Push
```bash
git init
git add .
git commit -m "Add Blackbird API"
git remote add origin https://github.com/YOUR_USERNAME/blackbird-api.git
git push -u origin main
```

### 2. Railway'de:
1. https://railway.app → GitHub ile giriş
2. "Deploy from GitHub repo"
3. Repo'yu seç
4. Variables → `PORT=8000` ekle
5. Deploy!

### 3. Test Et:
```bash
curl https://your-app.railway.app/
```

### 4. API'yi Kullan:
```
https://your-app.railway.app/docs
```

**HEPSİ BU KADAR! 🎉**

---

## 📞 Yardım

### Railway Support:
- Discord: https://discord.gg/railway
- Docs: https://docs.railway.app

### API Test:
```bash
# Health check
curl https://your-app.railway.app/

# Docs
open https://your-app.railway.app/docs
```

---

**Kolay gelsin! API'n Railway'de live olacak! 🚀**
