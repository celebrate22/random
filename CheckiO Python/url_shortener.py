
### Python Program: `url_shortener.py`

```python
import hashlib
import json
from pathlib import Path

class URLShortener:
    def __init__(self, storage_file="urls.json"):
        self.storage_file = Path(storage_file)
        self.urls = self._load()
    
    def _load(self):
        if self.storage_file.exists():
            with open(self.storage_file, 'r') as f:
                return json.load(f)
        return {}
    
    def _save(self):
        with open(self.storage_file, 'w') as f:
            json.dump(self.urls, f, indent=2)
    
    def shorten(self, url):
        short_id = hashlib.md5(url.encode()).hexdigest()[:6]
        self.urls[short_id] = url
        self._save()
        return f"short.ly/{short_id}"
    
    def expand(self, short_id):
        return self.urls.get(short_id, "URL not found")

if __name__ == "__main__":
    shortener = URLShortener()
    url = input("Enter URL: ")
    short = shortener.shorten(url)
    print(f"Shortened: {short}")
