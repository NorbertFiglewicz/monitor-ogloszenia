# check_ads.py
import json
import requests
from datetime import datetime

DATE = datetime.now().strftime("%Y-%m-%d %H:00")

with open("ads.json") as f:
    ads = json.load(f)

for ad in ads:
    try:
        r = requests.get(ad["url"], allow_redirects=True, timeout=10)
        status = "DOSTEPNE" if r.url == ad["url"] else "NIEDOSTEPNE"
    except:
        status = "NIEDOSTEPNE"

    filename = f"log_{ad['name'].replace(' ','_')}.csv"

    with open(filename, "a") as log:
        log.write(f"{DATE},{status}\n")