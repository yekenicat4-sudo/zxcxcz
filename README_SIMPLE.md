# 🦅 Blackbird API - Railway Deployment

Blackbird OSINT aracının FastAPI tabanlı REST API versiyonu. 600+ platformda kullanıcı adı ve e-posta araması yapın!

## 🚀 Hızlı Deploy (3 Adım)

### 1️⃣ GitHub'a Push
```bash
git init
git add .
git commit -m "Add Blackbird API"
git remote add origin https://github.com/YOUR_USERNAME/blackbird-api.git
git push -u origin main
```

### 2️⃣ Railway'de Deploy
1. https://railway.app → GitHub ile giriş
2. "Deploy from GitHub repo" → Repo seç
3. Variables → `PORT=8000`
4. Deploy!

### 3️⃣ Kullan
```bash
curl https://your-app.railway.app/
```

**API Docs**: `https://your-app.railway.app/docs`

---

## 📡 API Endpoints

### Health Check
```http
GET /
```

### Username Araması
```http
POST /search/username

{
  "username": "johndoe",
  "no_nsfw": false,
  "timeout": 30,
  "use_ai": false
}
```

### Email Araması
```http
POST /search/email

{
  "email": "test@example.com",
  "no_nsfw": false,
  "use_ai": false
}
```

---

## 💻 Kullanım Örnekleri

### Python
```python
import requests

response = requests.post(
    "https://your-app.railway.app/search/username",
    json={"username": "johndoe", "no_nsfw": True}
)

print(response.json())
```

### JavaScript
```javascript
const response = await fetch('https://your-app.railway.app/search/username', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ username: 'johndoe', no_nsfw: true })
});

const data = await response.json();
console.log(data);
```

### cURL
```bash
curl -X POST https://your-app.railway.app/search/username \
  -H "Content-Type: application/json" \
  -d '{"username": "johndoe"}'
```

---

## 📁 Önemli Dosyalar

| Dosya | Açıklama |
|-------|----------|
| `api.py` | FastAPI backend |
| `Dockerfile.api` | Railway Docker config |
| `railway.json` | Railway deployment config |
| `requirements-api.txt` | Python dependencies |
| `.env.example` | Environment variables template |

---

## ⚙️ Environment Variables (Railway)

```env
# Zorunlu
PORT=8000

# Opsiyonel
INSTAGRAM_SESSION_ID=your_session_id
```

---

## 🧪 Local Test (Opsiyonel)

```bash
# Bağımlılıkları yükle
pip install -r requirements-api.txt

# API'yi başlat
python api.py

# Test et
curl http://localhost:8000/
```

---

## 💰 Maliyet (Railway)

- **$5/ay** ücretsiz kredi
- **500 saat** execution time
- **8 GB RAM**

**Blackbird için YETERLI!**

---

## 📚 Detaylı Dokümantasyon

- **Railway Setup**: [RAILWAY_SETUP.md](RAILWAY_SETUP.md) - Adım adım deployment
- **Quick Start**: [QUICKSTART.md](QUICKSTART.md) - Hızlı başlangıç
- **Original Blackbird**: https://github.com/antoniaci/blackbird

---

## 🎯 Özellikler

✅ **600+ Platform** - WhatsMyName database  
✅ **Username Search** - Sosyal medya araması  
✅ **Email Search** - E-posta araması  
✅ **AI Analysis** - Opsiyonel profil analizi  
✅ **NSFW Filter** - Yetişkin içerik filtresi  
✅ **REST API** - Modern FastAPI  
✅ **Railway Ready** - Tek tıkla deploy  
✅ **Swagger Docs** - Interactive API docs  

---

## 🐛 Troubleshooting

### Deploy Failed?
- `Dockerfile.api` var mı kontrol et
- `PORT=8000` environment variable'ı ekle
- Build logs'u Railway'de kontrol et

### 502 Error?
- Deploy bitmesini bekle (2-3 dakika)
- Railway'i restart et

### Local Test Hatası?
```bash
pip install -r requirements-api.txt
PORT=8080 python api.py
```

---

## 📞 Support

- **Railway Docs**: https://docs.railway.app
- **Railway Discord**: https://discord.gg/railway
- **Original Blackbird**: https://github.com/antoniaci/blackbird

---

## ⚖️ License

Educational purposes only. Use responsibly.

**Original Blackbird**: [Lucas Antoniaci](https://github.com/antoniaci/blackbird)

---

**🎉 API'n hazır! Railway'e deploy et ve kullanmaya başla! 🚀**
