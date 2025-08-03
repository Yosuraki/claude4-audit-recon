# mmit_server.py
# Lightweight Flask server providing a POST API to log prompts + scores
# Used to connect GUI / CLI input sources to a shared reflex log store

from flask import Flask, request
import json
import datetime

app = Flask(__name__)

LOGFILE = "reflex_log.json"

@app.route("/log", methods=["POST"])
def log_prompt():
    data = request.json
    data["timestamp"] = str(datetime.datetime.now())

    try:
        with open(LOGFILE, "r") as f:
            logs = json.load(f)
    except:
        logs = []

    logs.append(data)
    with open(LOGFILE, "w") as f:
        json.dump(logs, f, indent=2)

    return {"status": "logged", "length": len(logs)}

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8500)
