import glob
import csv

html = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Monitoring LAN</title>
<style>
body { font-family: Arial; text-align: center; margin: 30px; }
.status { font-size: 40px; margin: 20px; font-weight: bold; }
.card { margin-bottom: 60px; }
.green { color: green; }
.red { color: red; }
img { border: 1px solid #ccc; border-radius: 8px; }
</style>
</head>
<body>
<h1>Monitoring LAN</h1>
"""

last_update = None

for file in glob.glob("log_*.csv"):
    name = file[4:-4]

    with open(file, newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))

        if rows:
            last_row = rows[-1]
            status = last_row[1]
            last_update = last_row[0]

            color = "green" if status == "DOSTEPNE" else "red"

            # szukamy odpowiadającego wykresu
            chart_file = f"chart_{name}.png"

            html += f"""
            <div class="card">
                <div class="status {color}">{status}</div>
                <div>{name}</div>
                <img src="{chart_file}" alt="{name}" style="max-width:600px; margin-top:10px;">
            </div>
            """

html += f"<p>Ostatnia zmiana: {last_update}</p>\n"
html += "</body></html>"

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
