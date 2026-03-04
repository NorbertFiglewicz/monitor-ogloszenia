# generate_page.py

import glob
import pandas as pd
import os

sections = ""

log_files = glob.glob("log_*.csv")

for file in log_files:
    name = file.replace("log_", "").replace(".csv", "")
    df = pd.read_csv(file, names=["datetime","status"])

    last_status = df.iloc[-1]["status"]

    if last_status == "DOSTEPNE":
        color = "green"
        icon = "🟢"
        text = "DOSTĘPNE"
    else:
        color = "red"
        icon = "🔴"
        text = "NIEDOSTĘPNE"

    sections += f"""
    <div class="card">
        <h2>{name.replace('_',' ')}</h2>
        <div class="status" style="color:{color}">{icon} {text}</div>
        <img src="chart_{name}.png" width="100%">
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
    margin: 30px;
}}
.status {{
    font-size: 40px;
    margin: 20px;
    font-weight: bold;
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

with open("index.html","w",encoding="utf-8") as f:
    f.write(html)
