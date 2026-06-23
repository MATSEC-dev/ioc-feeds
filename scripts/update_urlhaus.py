import requests
from pathlib import Path

FEED_URL = "https://urlhaus.abuse.ch/downloads/text/"

response = requests.get(FEED_URL, timeout=60)
response.raise_for_status()

Path("feeds").mkdir(exist_ok=True)

with open("feeds/urlhaus.txt", "w", encoding="utf-8") as f:
    f.write(response.text)

count = len([
    line for line in response.text.splitlines()
    if line.strip() and not line.startswith("#")
])

print(f"Downloaded {count:,} URLhaus entries")
