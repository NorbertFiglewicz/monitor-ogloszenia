import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import glob
import os

log_files = glob.glob("log_*.csv")

for file in log_files:
    name = file.replace("log_", "").replace(".csv", "")
    df = pd.read_csv(file, names=["datetime", "status"])
    df["datetime"] = pd.to_datetime(df["datetime"])

    # Filtr: ostatnie 3 miesiące
    three_months_ago = datetime.now() - timedelta(days=90)
    df = df[df["datetime"] >= three_months_ago]

    if df.empty:
        continue

    df["value"] = df["status"].apply(lambda x: 1 if x == "DOSTEPNE" else 0)
    availability_percent = round(df["value"].mean() * 100, 2)

    plt.figure(figsize=(12, 4))
    plt.plot(df["datetime"], df["value"], linewidth=1)
    plt.ylim(-0.1, 1.1)
    plt.yticks([0,1], ["NIEDOSTEPNE", "DOSTEPNE"])
    plt.title(f"{name} - ostatnie 3 miesiące ({availability_percent}%)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"chart_{name}.png")
    plt.close()
