# check_ads.py

from datetime import datetime
import requests
import os

DATE = datetime.now().strftime("%Y-%m-%d %H:00")

ads = []

with open("ads.secret.txt", "r", encoding="utf-8") as f:
    for line in f:
        if "|" in line:
            name, url = line.strip().split("|", 1)
            ads.append({"name": name, "url": url})

for ad in ads:
    try:
        r = requests.get(ad["url"], allow_redirects=True, timeout=15)
        status = "DOSTEPNE" if r.url == ad["url"] else "NIEDOSTEPNE"
    except:
        status = "NIEDOSTEPNE"

    filename = f"log_{ad['name'].replace(' ','_')}.csv"

    with open(filename, "a", encoding="utf-8") as log:
        log.write(f"{DATE},{status}\n")
