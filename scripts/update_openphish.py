import requests
from pathlib import Path

FEED_URL = "https://raw.githubusercontent.com/openphish/public_feed/refs/heads/main/feed.txt"

r = requests.get(FEED_URL, timeout=60)
r.raise_for_status()

Path("feeds").mkdir(exist_ok=True)

with open("feeds/openphish.txt", "w", encoding="utf-8") as f:
    f.write(r.text)

print(f"Downloaded {len(r.text.splitlines())} URLs")
