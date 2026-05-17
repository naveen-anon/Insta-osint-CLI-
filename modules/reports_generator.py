import json
import os
from datetime import datetime


def generate_report(target: str, data: dict):
    os.makedirs("output/reports", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    path = f"output/reports/{target}_{timestamp}.json"

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)

    return path
