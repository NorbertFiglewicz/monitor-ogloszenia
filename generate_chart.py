import pandas as pd
import matplotlib.pyplot as plt
import glob

for file in glob.glob("log_*.csv"):
    name = file[4:-4]  # usuń "log_" i ".csv"

    df = pd.read_csv(file, names=["datetime", "status"])
    df["datetime"] = pd.to_datetime(df["datetime"])
    df["value"] = df["status"].apply(lambda x: 1 if x == "DOSTEPNE" else 0)

    # ostatnie 90 dni
    cutoff = pd.Timestamp.now() - pd.Timedelta(days=90)
    df = df[df["datetime"] >= cutoff]

    plt.figure(figsize=(8, 4))
    plt.plot(df["datetime"], df["value"], drawstyle="steps-post", marker="o")
    plt.ylim(-0.1, 1.1)
    plt.yticks([0, 1], ["NIEDOSTEPNE", "DOSTEPNE"])
    plt.title(f"Status: {name}")
    plt.xlabel("Czas")
    plt.ylabel("Status")
    plt.grid(True)
    plt.tight_layout()

    # WAŻNE: spójna nazwa pliku
    plt.savefig(f"chart_{name}.png")
    plt.close()
