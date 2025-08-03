# reflex_gui.py
# A simple Tkinter-based frontend to log prompt-response pairs
# with user-scored cooperation and trigger sensitivity.

import tkinter as tk
from tkinter import messagebox
import json
import datetime

LOGFILE = "reflex_log.json"  # Target file for audit logging

def save_entry():
    try:
        # Parse float from input fields (comma or dot)
        coop_score = float(coop_entry.get().replace(",", "."))
        trigger_score = float(trigger_entry.get().replace(",", "."))
    except ValueError:
        messagebox.showerror("❌ Fehler", "Bitte gültige Zahlen für Scores eingeben.")
        return

    entry = {
        "timestamp": str(datetime.datetime.now()),
        "prompt": prompt_text.get("1.0", "end").strip(),
        "response": response_text.get("1.0", "end").strip(),
        "cooperation_score": coop_score,
        "trigger_score": trigger_score,
        "notes": notes_entry.get("1.0", "end").strip()
    }

    # Load existing file or create fresh
    try:
        with open(LOGFILE, "r") as f:
            data = json.load(f)
    except:
        data = []

    data.append(entry)
    with open(LOGFILE, "w") as f:
        json.dump(data, f, indent=2)

    messagebox.showinfo("✅ Gespeichert", "Prompt-Response gespeichert.")
    # Clear fields for next entry
    prompt_text.delete("1.0", "end")
    response_text.delete("1.0", "end")
    coop_entry.delete(0, "end")
    trigger_entry.delete(0, "end")
    notes_entry.delete("1.0", "end")

# GUI layout
root = tk.Tk()
root.title("Claude Reflex Logger")

tk.Label(root, text="🧠 Prompt").pack()
prompt_text = tk.Text(root, height=5)
prompt_text.pack()

tk.Label(root, text="💬 Response").pack()
response_text = tk.Text(root, height=5)
response_text.pack()

tk.Label(root, text="🤝 Cooperation Score (0–1)").pack()
coop_entry = tk.Entry(root)
coop_entry.pack()

tk.Label(root, text="🚨 Trigger Score (0–1)").pack()
trigger_entry = tk.Entry(root)
trigger_entry.pack()

tk.Label(root, text="📝 Notes (optional)").pack()
notes_entry = tk.Text(root, height=2)
notes_entry.pack()

tk.Button(root, text="💾 Speichern", command=save_entry).pack(pady=10)

root.mainloop()
