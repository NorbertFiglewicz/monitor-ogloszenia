import requests
from datetime import datetime
import os
import csv

# 🔒 Sekrety z GitHub (BASE_ANONS i BASE_MAIN)
BASE_ANONS = os.environ.get("BASE_ANONS")
BASE_MAIN = os.environ.get("BASE_MAIN")

if not BASE_ANONS or not BASE_MAIN:
    raise Exception("Brak secretów BASE_ANONS lub BASE_MAIN!")

# Wczytanie routerów i numerów z ads.json
ads = []
with open("ads.json", "r", encoding="utf-8") as f:
    for line in f:
        if "|" in line:
            name, number = line.strip().split("|")
            ads.append((name.strip(), number.strip()))

for ad_name, ad_number in ads:
    ad_url = f"{BASE_ANONS}{ad_number}.html"
    try:
        r = requests.get(ad_url, allow_redirects=True, timeout=10)
        status = "NIEDOSTEPNE" if r.url.rstrip("/") == BASE_MAIN else "DOSTEPNE"
    except:
        status = "NIEDOSTEPNE"

    csv_file = f"log_{ad_name}.csv"
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Dopisywanie logu
    if not os.path.exists(csv_file):
        with open(csv_file, "w", encoding="utf-8") as f:
            f.write(f"{now},{status}\n")
    else:
        with open(csv_file, "a", encoding="utf-8") as f:
            f.write(f"{now},{status}\n")
