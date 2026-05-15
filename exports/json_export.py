import os
import json

def save_json(username, scan_type, data):
    path = f"reports/scans/{username}"
    
    os.makedirs(path, exist_ok=True)

    with open(
        f"{path}/{scan_type}.json",
        "w"
    ) as f:
        json.dump(
            data,
            f,
            indent=4
        )
