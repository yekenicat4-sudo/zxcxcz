# 🚀 Hızlı Başlangıç Rehberi

## ⚡ 3 Adımda Railway'e Deploy

### 1. GitHub'a Push Et
```bash
# Repository başlat
cd blackbird-main
git init
git add .
git commit -m "Add Blackbird API"

# GitHub repo'na push et
git remote add origin https://github.com/YOUR_USERNAME/blackbird-api.git
git branch -M main
git push -u origin main
```

### 2. Railway'de Deploy Et
1. https://railway.app → GitHub ile giriş yap
2. "Deploy from GitHub repo" → Repo'yu seç
3. Variables → `PORT=8000` ekle
4. Deploy! 🚀

### 3. Test Et
```bash
# Railway URL'ini al (örn: https://blackbird-production.railway.app)
curl https://your-app.railway.app/

# API Docs
# Tarayıcıda aç: https://your-app.railway.app/docs
```

---

## 💻 Local Test (Opsiyonel)

### 1. Kurulum
```bash
pip install -r requirements-api.txt
```

### 2. API'yi Çalıştır
```bash
python api.py
```

API: `http://localhost:8000`  
Docs: `http://localhost:8000/docs`

### 3. Test Et
```bash
# Health check
curl http://localhost:8000/

# Username araması
curl -X POST http://localhost:8000/search/username \
  -H "Content-Type: application/json" \
  -d '{"username": "test"}'
```

---

## 📡 API Kullanımı

### Health Check
```bash
curl https://your-app.railway.app/
```

Response:
```json
{
  "status": "healthy",
  "version": "1.0.0",
  "sites_count": 600
}
```

### Username Search
```bash
curl -X POST https://your-app.railway.app/search/username \
  -H "Content-Type: application/json" \
  -d '{"username": "johndoe", "no_nsfw": true}'
```

### Email Search
```bash
curl -X POST https://your-app.railway.app/search/email \
  -H "Content-Type: application/json" \
  -d '{"email": "test@example.com"}'
```

## 📱 Kod Örnekleri

### Python
```python
import requests

API_URL = "https://your-app.railway.app"

response = requests.post(
    f"{API_URL}/search/username",
    json={"username": "johndoe", "no_nsfw": True}
)

data = response.json()
print(f"Bulundu: {data['total_found']} hesap")

for account in data['found_accounts']:
    print(f"  - {account['name']}: {account['url']}")
```

### JavaScript/Node.js
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

### cURL
```bash
curl -X POST https://your-app.railway.app/search/username \
  -H "Content-Type: application/json" \
  -d '{"username": "johndoe", "no_nsfw": true}'
```

## 🔧 Troubleshooting

### "Module not found" Hatası
```bash
pip install -r requirements-api.txt
```

### Port Zaten Kullanımda (Local)
```bash
PORT=8080 python api.py
```

### Railway Deploy Başarısız
1. `Dockerfile.api` dosyası var mı?
2. Environment variables: `PORT=8000` var mı?
3. Build logs'u kontrol et
4. Railway'i restart dene

## 💡 İpuçları

- **AI Özelliği**: `python blackbird.py --setup-ai` ile API key al
- **Hız**: `max_concurrent_requests` değerini ayarla (varsayılan: 30)
- **NSFW**: `no_nsfw: true` ile yetişkin içerikli siteleri filtrele
- **Docs**: Railway URL + `/docs` → Interactive API dokümantasyonu

## 📚 Daha Fazla Bilgi

- **Railway Setup**: [RAILWAY_SETUP.md](RAILWAY_SETUP.md) ⭐
- **API Dokümantasyonu**: `https://your-app.railway.app/docs`
- **Original Blackbird**: https://github.com/antoniaci/blackbird

## 💰 Maliyet (Railway)

- **$5/ay** ücretsiz kredi
- **500 saat** execution time
- Blackbird için **YETERLI!**

---

**🎉 3 Adımda Deploy Et!**

1. GitHub'a push et
2. Railway'de deploy et  
3. API'ni kullan!

**Detaylı rehber: [RAILWAY_SETUP.md](RAILWAY_SETUP.md)**
