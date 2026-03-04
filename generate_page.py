# generate_page.py

import pandas as pd
from datetime import datetime
import glob

log_files = glob.glob("log_*.csv")

# Pobierz aktualny czas (ostatnia aktualizacja)
last_update = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

html_content = f"""<!DOCTYPE html>
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
.last-update {{
    font-size: 16px;
    margin-top: 20px;
    color: #555;
}}
</style>
</head>
<body>
<h1>Monitoring ogłoszeń</h1>
"""

for file in log_files:
    name = file.replace("log_", "").replace(".csv", "")
    df = pd.read_csv(file, names=["datetime", "status"])
    latest_status = df["status"].iloc[-1] if not df.empty else "BRAK DANYCH"
    color = "green" if latest_status.upper() == "DOSTEPNE" else "red"

    html_content += f"""
<div class="card">
    <div class="status" style="color:{color}">{latest_status}</div>
    <div>{name}</div>
</div>
"""

# Dodaj ostatnią aktualizację na dole strony
html_content += f"""
<div class="last-update">
    Ostatnia aktualizacja: {last_update}
</div>
"""

html_content += """
</body>
</html>
"""

# Zapisz do pliku
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)
