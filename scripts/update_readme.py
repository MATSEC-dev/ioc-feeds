from pathlib import Path
from datetime import datetime

feed_file = Path("feeds/openphish.txt")

if feed_file.exists():
    count = sum(1 for line in feed_file.read_text(
        encoding="utf-8"
    ).splitlines() if line.strip())
else:
    count = 0

timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

readme = f"""# OpenPhish Feed Mirror

This repository mirrors the public OpenPhish feed.

## Statistics

| Metric | Value |
|---------|---------|
| URLs | {count:,} |
| Last Updated (UTC) | {timestamp} |

## Feed

- `feeds/openphish.txt`
"""

Path("README.md").write_text(readme, encoding="utf-8")

print(f"README updated ({count:,} URLs)")
