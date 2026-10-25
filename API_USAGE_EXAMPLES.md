# 🎯 Blackbird API - Kullanım Örnekleri

**API URL:** `https://zxcxcz-production.up.railway.app`

---

## 🌐 API Endpoints

### 1. Health Check
```
GET https://zxcxcz-production.up.railway.app/
```

### 2. Username Search
```
POST https://zxcxcz-production.up.railway.app/search/username
```

### 3. Email Search
```
POST https://zxcxcz-production.up.railway.app/search/email
```

### 4. API Documentation (Interactive)
```
https://zxcxcz-production.up.railway.app/docs
```

---

## 💻 Kullanım Örnekleri

### 🔹 Health Check

#### cURL
```bash
curl https://zxcxcz-production.up.railway.app/
```

#### Python
```python
import requests

response = requests.get("https://zxcxcz-production.up.railway.app/")
print(response.json())
```

#### Response
```json
{
  "status": "healthy",
  "version": "1.0.0",
  "sites_count": 6
}
```

---

### 🔹 Username Search

#### cURL
```bash
curl -X POST https://zxcxcz-production.up.railway.app/search/username \
  -H "Content-Type: application/json" \
  -d '{"username": "johndoe", "no_nsfw": true}'
```

#### Python
```python
import requests
import json

url = "https://zxcxcz-production.up.railway.app/search/username"

payload = {
    "username": "johndoe",
    "no_nsfw": True,
    "timeout": 30,
    "max_concurrent_requests": 30,
    "use_ai": False
}

response = requests.post(url, json=payload)
data = response.json()

print(f"Query: {data['query']}")
print(f"Total Found: {data['total_found']}")
print(f"\nAccounts:")

for account in data['found_accounts']:
    print(f"  - {account['name']}: {account['url']}")
```

#### JavaScript/Node.js
```javascript
const axios = require('axios');

const url = 'https://zxcxcz-production.up.railway.app/search/username';

const payload = {
  username: 'johndoe',
  no_nsfw: true,
  timeout: 30,
  max_concurrent_requests: 30,
  use_ai: false
};

axios.post(url, payload)
  .then(response => {
    const data = response.data;
    console.log(`Query: ${data.query}`);
    console.log(`Total Found: ${data.total_found}`);
    
    data.found_accounts.forEach(account => {
      console.log(`  - ${account.name}: ${account.url}`);
    });
  })
  .catch(error => console.error('Error:', error));
```

#### JavaScript/Fetch (Browser)
```javascript
const url = 'https://zxcxcz-production.up.railway.app/search/username';

const payload = {
  username: 'johndoe',
  no_nsfw: true,
  timeout: 30,
  use_ai: false
};

fetch(url, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify(payload)
})
  .then(response => response.json())
  .then(data => {
    console.log(`Found ${data.total_found} accounts`);
    data.found_accounts.forEach(account => {
      console.log(`${account.name}: ${account.url}`);
    });
  })
  .catch(error => console.error('Error:', error));
```

#### Response Example
```json
{
  "query": "johndoe",
  "query_type": "username",
  "found_accounts": [
    {
      "name": "GitHub",
      "url": "https://github.com/johndoe",
      "cat": "coding",
      "uri_check": "https://github.com/johndoe"
    },
    {
      "name": "Twitter",
      "url": "https://twitter.com/johndoe",
      "cat": "social",
      "uri_check": "https://twitter.com/johndoe"
    }
  ],
  "total_found": 2,
  "search_date": "2024-01-15 10:30:00",
  "ai_analysis": null
}
```

---

### 🔹 Email Search

#### cURL
```bash
curl -X POST https://zxcxcz-production.up.railway.app/search/email \
  -H "Content-Type: application/json" \
  -d '{"email": "test@example.com", "no_nsfw": true}'
```

#### Python
```python
import requests

url = "https://zxcxcz-production.up.railway.app/search/email"

payload = {
    "email": "test@example.com",
    "no_nsfw": True,
    "timeout": 30,
    "use_ai": False
}

response = requests.post(url, json=payload)
data = response.json()

print(f"Email: {data['query']}")
print(f"Total Found: {data['total_found']}")

for account in data['found_accounts']:
    print(f"  - {account['name']}: {account['url']}")
```

#### JavaScript
```javascript
const url = 'https://zxcxcz-production.up.railway.app/search/email';

const payload = {
  email: 'test@example.com',
  no_nsfw: true,
  timeout: 30,
  use_ai: false
};

fetch(url, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify(payload)
})
  .then(response => response.json())
  .then(data => {
    console.log(`Found ${data.total_found} accounts for ${data.query}`);
    data.found_accounts.forEach(account => {
      console.log(`  - ${account.name}: ${account.url}`);
    });
  });
```

---

## 🔧 Advanced Options

### All Parameters

```json
{
  "username": "johndoe",           // Required for username search
  "email": "test@example.com",     // Required for email search
  "filter": null,                  // Optional: Filter by category (e.g., "cat=social")
  "no_nsfw": false,                // Optional: Exclude NSFW sites
  "timeout": 30,                   // Optional: Request timeout in seconds (default: 30)
  "max_concurrent_requests": 30,   // Optional: Max concurrent requests (default: 30)
  "use_ai": false                  // Optional: Enable AI analysis (requires API key)
}
```

### Example with AI Analysis
```bash
curl -X POST https://zxcxcz-production.up.railway.app/search/username \
  -H "Content-Type: application/json" \
  -d '{
    "username": "johndoe",
    "no_nsfw": true,
    "use_ai": true
  }'
```

### Example with Category Filter
```bash
curl -X POST https://zxcxcz-production.up.railway.app/search/username \
  -H "Content-Type: application/json" \
  -d '{
    "username": "johndoe",
    "filter": "cat=social"
  }'
```

---

## 🐍 Python Script - Tam Örnek

```python
#!/usr/bin/env python3
"""
Blackbird API Client Example
"""

import requests
import json
from typing import Optional

class BlackbirdAPI:
    def __init__(self, base_url: str = "https://zxcxcz-production.up.railway.app"):
        self.base_url = base_url
    
    def health_check(self) -> dict:
        """Check API health"""
        response = requests.get(f"{self.base_url}/")
        return response.json()
    
    def search_username(
        self,
        username: str,
        no_nsfw: bool = False,
        use_ai: bool = False,
        timeout: int = 30,
        max_concurrent: int = 30,
        filter_cat: Optional[str] = None
    ) -> dict:
        """Search for username across platforms"""
        url = f"{self.base_url}/search/username"
        
        payload = {
            "username": username,
            "no_nsfw": no_nsfw,
            "timeout": timeout,
            "max_concurrent_requests": max_concurrent,
            "use_ai": use_ai
        }
        
        if filter_cat:
            payload["filter"] = f"cat={filter_cat}"
        
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()
    
    def search_email(
        self,
        email: str,
        no_nsfw: bool = False,
        use_ai: bool = False,
        timeout: int = 30
    ) -> dict:
        """Search for email across platforms"""
        url = f"{self.base_url}/search/email"
        
        payload = {
            "email": email,
            "no_nsfw": no_nsfw,
            "timeout": timeout,
            "use_ai": use_ai
        }
        
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()


# Usage Example
if __name__ == "__main__":
    api = BlackbirdAPI()
    
    # Health check
    print("🔍 Checking API health...")
    health = api.health_check()
    print(f"✅ Status: {health['status']}")
    print(f"📊 Sites available: {health['sites_count']}\n")
    
    # Username search
    print("🔍 Searching for username: johndoe")
    result = api.search_username(
        username="johndoe",
        no_nsfw=True,
        use_ai=False
    )
    
    print(f"✅ Found {result['total_found']} accounts:\n")
    
    for account in result['found_accounts']:
        name = account.get('name', 'Unknown')
        url = account.get('url', 'N/A')
        category = account.get('cat', 'Unknown')
        
        print(f"  🌐 {name}")
        print(f"     Category: {category}")
        print(f"     URL: {url}\n")
    
    # Save results to JSON
    with open('blackbird_results.json', 'w') as f:
        json.dump(result, f, indent=2)
    
    print("💾 Results saved to blackbird_results.json")
```

---

## 🌐 Web Integration Example (HTML + JS)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blackbird API Demo</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
        }
        input, button {
            padding: 10px;
            margin: 5px;
            font-size: 16px;
        }
        button {
            background-color: #dc143c;
            color: white;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #b01030;
        }
        #results {
            margin-top: 20px;
        }
        .account {
            border: 1px solid #ddd;
            padding: 10px;
            margin: 10px 0;
            border-radius: 5px;
        }
        .loading {
            color: #666;
            font-style: italic;
        }
    </style>
</head>
<body>
    <h1>🦅 Blackbird OSINT Search</h1>
    
    <div>
        <input type="text" id="username" placeholder="Enter username" />
        <button onclick="searchUsername()">Search Username</button>
    </div>
    
    <div id="results"></div>

    <script>
        const API_URL = 'https://zxcxcz-production.up.railway.app';

        async function searchUsername() {
            const username = document.getElementById('username').value;
            const resultsDiv = document.getElementById('results');
            
            if (!username) {
                alert('Please enter a username');
                return;
            }
            
            resultsDiv.innerHTML = '<p class="loading">🔍 Searching...</p>';
            
            try {
                const response = await fetch(`${API_URL}/search/username`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        username: username,
                        no_nsfw: true,
                        timeout: 30
                    })
                });
                
                const data = await response.json();
                
                if (data.total_found === 0) {
                    resultsDiv.innerHTML = '<p>❌ No accounts found</p>';
                    return;
                }
                
                let html = `<h2>✅ Found ${data.total_found} accounts</h2>`;
                
                data.found_accounts.forEach(account => {
                    html += `
                        <div class="account">
                            <h3>🌐 ${account.name}</h3>
                            <p><strong>Category:</strong> ${account.cat || 'Unknown'}</p>
                            <p><strong>URL:</strong> <a href="${account.url}" target="_blank">${account.url}</a></p>
                        </div>
                    `;
                });
                
                resultsDiv.innerHTML = html;
                
            } catch (error) {
                resultsDiv.innerHTML = `<p>❌ Error: ${error.message}</p>`;
            }
        }
    </script>
</body>
</html>
```

---

## 📱 Mobile App Integration (React Native)

```javascript
import React, { useState } from 'react';
import { View, TextInput, Button, Text, FlatList } from 'react-native';

const BlackbirdSearch = () => {
  const [username, setUsername] = useState('');
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);

  const searchUsername = async () => {
    setLoading(true);
    
    try {
      const response = await fetch('https://zxcxcz-production.up.railway.app/search/username', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          username: username,
          no_nsfw: true,
          timeout: 30
        })
      });
      
      const data = await response.json();
      setResults(data.found_accounts);
    } catch (error) {
      console.error('Error:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <View style={{ padding: 20 }}>
      <TextInput
        placeholder="Enter username"
        value={username}
        onChangeText={setUsername}
        style={{ borderWidth: 1, padding: 10, marginBottom: 10 }}
      />
      
      <Button title="Search" onPress={searchUsername} />
      
      {loading && <Text>Searching...</Text>}
      
      <FlatList
        data={results}
        keyExtractor={(item, index) => index.toString()}
        renderItem={({ item }) => (
          <View style={{ padding: 10, borderWidth: 1, marginTop: 10 }}>
            <Text style={{ fontWeight: 'bold' }}>{item.name}</Text>
            <Text>Category: {item.cat}</Text>
            <Text>URL: {item.url}</Text>
          </View>
        )}
      />
    </View>
  );
};

export default BlackbirdSearch;
```

---

## 🎯 Best Practices

### 1. Error Handling
```python
import requests

try:
    response = requests.post(
        "https://zxcxcz-production.up.railway.app/search/username",
        json={"username": "test"},
        timeout=60
    )
    response.raise_for_status()
    data = response.json()
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.HTTPError as e:
    print(f"HTTP error: {e}")
except Exception as e:
    print(f"Error: {e}")
```

### 2. Rate Limiting (Client Side)
```python
import time

def search_with_delay(usernames, delay=2):
    results = []
    for username in usernames:
        result = search_username(username)
        results.append(result)
        time.sleep(delay)  # Wait between requests
    return results
```

### 3. Async Requests (Python)
```python
import asyncio
import aiohttp

async def search_async(username):
    url = "https://zxcxcz-production.up.railway.app/search/username"
    
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json={"username": username}) as response:
            return await response.json()

# Usage
results = asyncio.run(search_async("johndoe"))
```

---

## 📊 Response Codes

| Code | Meaning | Action |
|------|---------|--------|
| 200 | Success | Process response data |
| 422 | Validation Error | Check request payload |
| 500 | Server Error | Retry or contact support |
| 502 | Bad Gateway | Wait and retry (server starting) |
| 503 | Service Unavailable | Wait and retry |

---

## 🔗 Useful Links

- **API Documentation (Interactive):** https://zxcxcz-production.up.railway.app/docs
- **Alternative Docs (ReDoc):** https://zxcxcz-production.up.railway.app/redoc
- **OpenAPI Schema:** https://zxcxcz-production.up.railway.app/openapi.json

---

**🎉 API'niz hazır ve kullanıma hazır! İyi aramalar! 🚀**
