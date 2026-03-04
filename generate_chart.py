import pandas as pd
import matplotlib.pyplot as plt
import json
from datetime import datetime, timedelta
import os

with open("ads.json") as f:
    ads = json.load(f)

for ad in ads:
    name = ad["name"]
    filename = f"log_{name.replace(' ','_')}.csv"

    if not os.path.exists(filename):
        continue

    df = pd.read_csv(filename, names=["datetime", "status"])
    df["datetime"] = pd.to_datetime(df["datetime"])

    one_year_ago = datetime.now() - timedelta(days=365)
    df = df[df["datetime"] >= one_year_ago]

    if df.empty:
        continue

    df["value"] = df["status"].apply(lambda x: 1 if x == "DOSTEPNE" else 0)
    availability_percent = round(df["value"].mean() * 100, 2)

    plt.figure(figsize=(14,5))
    plt.plot(df["datetime"], df["value"], linewidth=1)
    plt.ylim(-0.1,1.1)
    plt.yticks([0,1], ["NIEDOSTEPNE","DOSTEPNE"])
    plt.title(f"{name} - ostatnie 12 miesiecy ({availability_percent}%)")
    plt.xticks(rotation=45)
    plt.tight_layout()

    chart_name = f"chart_{name.replace(' ','_')}.png"
    plt.savefig(chart_name)
    plt.close()