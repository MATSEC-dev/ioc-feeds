from pathlib import Path
from datetime import datetime

def count_entries(filename):
    path = Path(filename)

    if not path.exists():
        return 0

    return len([
        line for line in path.read_text(
            encoding="utf-8"
        ).splitlines()
        if line.strip() and not line.startswith("#")
    ])

openphish_count = count_entries("feeds/openphish.txt")
urlhaus_count = count_entries("feeds/urlhaus.txt")

total = openphish_count + urlhaus_count

timestamp = datetime.utcnow().strftime(
    "%Y-%m-%d %H:%M:%S UTC"
)

readme = f"""# Threat Intelligence Feed Mirror

Automatically updated IOC feeds.

## Statistics

| Feed | Count |
|--------|--------:|
| OpenPhish URLs | {openphish_count:,} |
| URLhaus URLs | {urlhaus_count:,} |
| Total IOCs | {total:,} |

Last Updated: **{timestamp}**

## Available Feeds

- feeds/openphish.txt
- feeds/urlhaus.txt
"""

Path("README.md").write_text(
    readme,
    encoding="utf-8"
)

print("README updated")
