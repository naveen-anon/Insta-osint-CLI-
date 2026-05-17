# File: modules/export.py
import json
import os


def export_json(username, data):
    os.makedirs("output/json", exist_ok=True)

    path = f"output/json/{username}.json"

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    return path


