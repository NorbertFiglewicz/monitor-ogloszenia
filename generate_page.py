import json
import pandas as pd
import os

with open("ads.json") as f:
    ads = json.load(f)

sections = ""

for ad in ads:
    name = ad["name"]
    filename = f"log_{name.replace(' ','_')}.csv"
    chart_name = f"chart_{name.replace(' ','_')}.png"

    if not os.path.exists(filename):
        continue

    df = pd.read_csv(filename, names=["datetime", "status"])
    last_status = df.iloc[-1]["status"]

    color = "green" if last_status=="DOSTEPNE" else "red"
    icon = "✅" if last_status=="DOSTEPNE" else "❌"

    sections += f"""
    <div class="card">
        <h2>{name}</h2>
        <div class="status" style="color:{color}">{icon} {last_status}</div>
        <img src="{chart_name}" width="900">
    </div>
    <hr>
    """

html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Monitoring ogłoszeń</title>
<style>
body {{
    font-family: Arial;
    text-align: center;
    margin: 50px;
}}
.status {{
    font-size: 50px;
    margin: 20px;
}}
.card {{
    margin-bottom: 60px;
}}
</style>
</head>
<body>
<h1>Monitoring ogłoszeń</h1>
{sections}
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)