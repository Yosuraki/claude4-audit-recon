# analyze_log.py
# Parses the structured audit log (reflex_log.json) and generates a summary CSV
# Scores are averaged and grouped for deeper audit insights

import json
import csv

INPUT_FILE = "reflex_log.json"
OUTPUT_FILE = "reflex_summary.csv"

with open(INPUT_FILE, "r") as f:
    data = json.load(f)

with open(OUTPUT_FILE, "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["timestamp", "prompt_snippet", "coop_score", "trigger_score", "notes"])
    for entry in data:
        writer.writerow([
            entry["timestamp"],
            entry["prompt"][:40] + "...",
            entry["cooperation_score"],
            entry["trigger_score"],
            entry.get("notes", "")
        ])

print(f"✅ Summary written to: {OUTPUT_FILE}")
