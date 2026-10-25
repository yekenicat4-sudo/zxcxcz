# 🚀 Blackbird API - GET Endpoint Kullanımı

## 🎯 Basit URL ile Arama

Artık direkt URL'ye username yazarak arama yapabilirsin!

**API URL:** `https://zxcxcz-production.up.railway.app`

---

## 📡 GET Endpoints

### 1. Username Search (GET)
```
GET /search/username/{username}
```

### 2. Email Search (GET)
```
GET /search/email/{email}
```

---

## 💻 Kullanım Örnekleri

### 🔹 Username Ara

#### Basit Kullanım
```
https://zxcxcz-production.up.railway.app/search/username/argo4k
```

Tarayıcıda bu URL'i aç ve JSON sonuçları göreceksin!

#### NSFW Filtreli
```
https://zxcxcz-production.up.railway.app/search/username/argo4k?no_nsfw=true
```

#### Kategori Filtreli
```
https://zxcxcz-production.up.railway.app/search/username/argo4k?filter=cat%3Dsocial
```

#### Tüm Parametreler
```
https://zxcxcz-production.up.railway.app/search/username/argo4k?no_nsfw=true&timeout=30&max_concurrent_requests=20
```

---

### 🔹 Email Ara

#### Basit Kullanım
```
https://zxcxcz-production.up.railway.app/search/email/test@example.com
```

#### NSFW Filtreli
```
https://zxcxcz-production.up.railway.app/search/email/test@example.com?no_nsfw=true
```

---

## 🌐 Tarayıcıda Test Et

### Argo4k Ara
Direkt tıkla: [https://zxcxcz-production.up.railway.app/search/username/argo4k](https://zxcxcz-production.up.railway.app/search/username/argo4k)

### Test Username Ara
Direkt tıkla: [https://zxcxcz-production.up.railway.app/search/username/test](https://zxcxcz-production.up.railway.app/search/username/test)

### Email Ara
Direkt tıkla: [https://zxcxcz-production.up.railway.app/search/email/test@example.com](https://zxcxcz-production.up.railway.app/search/email/test@example.com)

---

## 💻 Kod Örnekleri

### JavaScript/Fetch
```javascript
// Basit GET request
fetch('https://zxcxcz-production.up.railway.app/search/username/argo4k')
  .then(response => response.json())
  .then(data => {
    console.log(`Bulundu: ${data.total_found} hesap`);
    data.found_accounts.forEach(acc => {
      console.log(`${acc.name}: ${acc.url}`);
    });
  });

// Parametreli
fetch('https://zxcxcz-production.up.railway.app/search/username/argo4k?no_nsfw=true&timeout=30')
  .then(response => response.json())
  .then(data => console.log(data));
```

### Python/Requests
```python
import requests

# Basit GET
response = requests.get(
    "https://zxcxcz-production.up.railway.app/search/username/argo4k"
)
data = response.json()

print(f"Bulundu: {data['total_found']} hesap")
for account in data['found_accounts']:
    print(f"  {account['name']}: {account['url']}")

# Parametreli
response = requests.get(
    "https://zxcxcz-production.up.railway.app/search/username/argo4k",
    params={"no_nsfw": True, "timeout": 30}
)
print(response.json())
```

### PowerShell
```powershell
# Basit GET
Invoke-RestMethod "https://zxcxcz-production.up.railway.app/search/username/argo4k"

# Parametreli
$params = @{
    no_nsfw = $true
    timeout = 30
}
Invoke-RestMethod "https://zxcxcz-production.up.railway.app/search/username/argo4k" -Body $params
```

### cURL
```bash
# Basit
curl "https://zxcxcz-production.up.railway.app/search/username/argo4k"

# Parametreli
curl "https://zxcxcz-production.up.railway.app/search/username/argo4k?no_nsfw=true&timeout=30"

# Email
curl "https://zxcxcz-production.up.railway.app/search/email/test@example.com?no_nsfw=true"
```

---

## 📊 Response Formatı

### Başarılı Response
```json
{
  "query": "argo4k",
  "query_type": "username",
  "found_accounts": [
    {
      "name": "Docker Hub",
      "url": "https://hub.docker.com/v2/users/argo4k/",
      "category": "coding",
      "status": "FOUND"
    },
    {
      "name": "YouTube",
      "url": "https://www.youtube.com/@argo4k",
      "category": "video",
      "status": "FOUND"
    }
  ],
  "total_found": 10,
  "search_date": "2026-10-25 10:30:00",
  "ai_analysis": null
}
```

---

## 🔧 Query Parameters

### Username Search
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `no_nsfw` | boolean | false | Exclude NSFW sites |
| `use_ai` | boolean | false | Enable AI analysis |
| `timeout` | integer | 30 | Request timeout (seconds) |
| `max_concurrent_requests` | integer | 30 | Max concurrent requests |
| `filter` | string | null | Filter by category (e.g., "cat=social") |

### Email Search
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `no_nsfw` | boolean | false | Exclude NSFW sites |
| `use_ai` | boolean | false | Enable AI analysis |
| `timeout` | integer | 30 | Request timeout (seconds) |
| `filter` | string | null | Filter by category |

---

## 🎨 HTML Örneği

Basit bir web sayfası:

```html
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>Blackbird Username Search</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
        }
        input {
            padding: 10px;
            font-size: 16px;
            width: 300px;
        }
        button {
            padding: 10px 20px;
            background: #dc143c;
            color: white;
            border: none;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background: #b01030;
        }
        .result {
            border: 1px solid #ddd;
            padding: 15px;
            margin: 10px 0;
            border-radius: 5px;
        }
        .result h3 {
            margin: 0 0 10px 0;
            color: #dc143c;
        }
        #loading {
            display: none;
            color: #666;
            font-style: italic;
        }
    </style>
</head>
<body>
    <h1>🦅 Blackbird Username Search</h1>
    
    <div>
        <input type="text" id="username" placeholder="Kullanıcı adı gir..." value="argo4k">
        <button onclick="searchUsername()">Ara</button>
        <label>
            <input type="checkbox" id="no_nsfw" checked> NSFW Filtrele
        </label>
    </div>
    
    <div id="loading">🔍 Aranıyor...</div>
    <div id="results"></div>

    <script>
        async function searchUsername() {
            const username = document.getElementById('username').value;
            const noNsfw = document.getElementById('no_nsfw').checked;
            const resultsDiv = document.getElementById('results');
            const loadingDiv = document.getElementById('loading');
            
            if (!username) {
                alert('Lütfen bir kullanıcı adı gir');
                return;
            }
            
            // Show loading
            loadingDiv.style.display = 'block';
            resultsDiv.innerHTML = '';
            
            try {
                // Simple GET request
                const url = `https://zxcxcz-production.up.railway.app/search/username/${username}?no_nsfw=${noNsfw}`;
                const response = await fetch(url);
                const data = await response.json();
                
                // Hide loading
                loadingDiv.style.display = 'none';
                
                if (data.total_found === 0) {
                    resultsDiv.innerHTML = '<p>❌ Hesap bulunamadı</p>';
                    return;
                }
                
                // Display results
                let html = `<h2>✅ ${data.total_found} Hesap Bulundu</h2>`;
                
                data.found_accounts.forEach(account => {
                    html += `
                        <div class="result">
                            <h3>🌐 ${account.name}</h3>
                            <p><strong>Kategori:</strong> ${account.category || 'Bilinmiyor'}</p>
                            <p><strong>URL:</strong> <a href="${account.url}" target="_blank">${account.url}</a></p>
                        </div>
                    `;
                });
                
                resultsDiv.innerHTML = html;
                
            } catch (error) {
                loadingDiv.style.display = 'none';
                resultsDiv.innerHTML = `<p style="color: red;">❌ Hata: ${error.message}</p>`;
            }
        }
        
        // Enter tuşu ile ara
        document.getElementById('username').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                searchUsername();
            }
        });
    </script>
</body>
</html>
```

Bu HTML'i `blackbird_search.html` olarak kaydet ve tarayıcıda aç!

---

## 📱 Mobile/React Native Örneği

```javascript
import React, { useState } from 'react';
import { View, TextInput, Button, Text, FlatList, ActivityIndicator } from 'react-native';

const BlackbirdSearch = () => {
  const [username, setUsername] = useState('argo4k');
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [totalFound, setTotalFound] = useState(0);

  const searchUsername = async () => {
    setLoading(true);
    
    try {
      // Simple GET request
      const url = `https://zxcxcz-production.up.railway.app/search/username/${username}?no_nsfw=true`;
      const response = await fetch(url);
      const data = await response.json();
      
      setResults(data.found_accounts);
      setTotalFound(data.total_found);
    } catch (error) {
      console.error('Error:', error);
      alert('Arama başarısız!');
    } finally {
      setLoading(false);
    }
  };

  return (
    <View style={{ padding: 20 }}>
      <Text style={{ fontSize: 24, fontWeight: 'bold', marginBottom: 20 }}>
        🦅 Blackbird Search
      </Text>
      
      <TextInput
        placeholder="Kullanıcı adı"
        value={username}
        onChangeText={setUsername}
        style={{
          borderWidth: 1,
          borderColor: '#ddd',
          padding: 10,
          marginBottom: 10,
          borderRadius: 5
        }}
      />
      
      <Button title="Ara" onPress={searchUsername} color="#dc143c" />
      
      {loading && <ActivityIndicator style={{ marginTop: 20 }} size="large" />}
      
      {!loading && totalFound > 0 && (
        <Text style={{ marginTop: 20, fontSize: 18, fontWeight: 'bold' }}>
          ✅ {totalFound} hesap bulundu
        </Text>
      )}
      
      <FlatList
        data={results}
        keyExtractor={(item, index) => index.toString()}
        renderItem={({ item }) => (
          <View style={{
            padding: 15,
            borderWidth: 1,
            borderColor: '#ddd',
            marginTop: 10,
            borderRadius: 5
          }}>
            <Text style={{ fontWeight: 'bold', fontSize: 16 }}>
              🌐 {item.name}
            </Text>
            <Text style={{ color: '#666', marginTop: 5 }}>
              Kategori: {item.category || 'Bilinmiyor'}
            </Text>
            <Text style={{ color: '#007AFF', marginTop: 5 }}>
              {item.url}
            </Text>
          </View>
        )}
      />
    </View>
  );
};

export default BlackbirdSearch;
```

---

## 🔗 Hızlı Linkler

### Test Linkleri (Direkt Tıkla)
- [Argo4k Ara](https://zxcxcz-production.up.railway.app/search/username/argo4k?no_nsfw=true)
- [Test Kullanıcısı Ara](https://zxcxcz-production.up.railway.app/search/username/test?no_nsfw=true)
- [Test Email Ara](https://zxcxcz-production.up.railway.app/search/email/test@example.com?no_nsfw=true)

### Dokümantasyon
- **API Docs:** https://zxcxcz-production.up.railway.app/docs
- **Health Check:** https://zxcxcz-production.up.railway.app/
- **ReDoc:** https://zxcxcz-production.up.railway.app/redoc

---

## 📊 POST vs GET Karşılaştırması

### POST (JSON Body)
```bash
curl -X POST https://zxcxcz-production.up.railway.app/search/username \
  -H "Content-Type: application/json" \
  -d '{"username": "argo4k", "no_nsfw": true}'
```

### GET (URL Parameters)
```bash
curl "https://zxcxcz-production.up.railway.app/search/username/argo4k?no_nsfw=true"
```

**GET daha basit!** Tarayıcıda direkt açabilirsin.

---

## 🎯 Senin İçin Hızlı Testler

### PowerShell
```powershell
# Argo4k ara
Invoke-RestMethod "https://zxcxcz-production.up.railway.app/search/username/argo4k?no_nsfw=true"

# Başka kullanıcı
Invoke-RestMethod "https://zxcxcz-production.up.railway.app/search/username/johndoe?no_nsfw=true"
```

### Python Script
```python
import requests

# Kullanıcı adı listesi
usernames = ["argo4k", "test", "johndoe"]

for username in usernames:
    url = f"https://zxcxcz-production.up.railway.app/search/username/{username}"
    response = requests.get(url, params={"no_nsfw": True})
    data = response.json()
    
    print(f"\n{username}: {data['total_found']} hesap bulundu")
    for acc in data['found_accounts'][:3]:
        print(f"  - {acc['name']}")
```

---

**🎉 Artık direkt URL'ye yazarak arama yapabilirsin!**

**Tarayıcıda dene: https://zxcxcz-production.up.railway.app/search/username/argo4k**
