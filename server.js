// server.js
import express from "express";
import fetch from "node-fetch";
import dotenv from "dotenv";

dotenv.config();

const app = express();
app.use(express.json());

const PORT = process.env.PORT || 3000;
const GITHUB_TOKEN = process.env.GH_TOKEN; // w pliku .env lub zmienna środowiskowa
const REPO = "NorbertFiglewicz/monitor-ogloszenia";
const WORKFLOW_ID = "add_ad.yml"; // nazwa workflow

app.post("/add-ad", async (req, res) => {
  const { name, number } = req.body;
  if (!name || !number) return res.status(400).json({ message: "Brak name lub number" });

  try {
    const response = await fetch(`https://api.github.com/repos/${REPO}/actions/workflows/${WORKFLOW_ID}/dispatches`, {
      method: "POST",
      headers: {
        "Accept": "application/vnd.github+json",
        "Authorization": `token ${GITHUB_TOKEN}`
      },
      body: JSON.stringify({
        ref: "main",
        inputs: { name, number }
      })
    });

    if (!response.ok) {
      const err = await response.json();
      return res.status(response.status).json({ message: err.message });
    }

    res.json({ message: `Workflow dla ${name}|${number} uruchomiony` });
  } catch (err) {
    res.status(500).json({ message: err.toString() });
  }
});

app.listen(PORT, () => {
  console.log(`Backend działa na http://localhost:${PORT}`);
});
