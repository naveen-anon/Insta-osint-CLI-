# exports/csv_export.py
import csv
from pathlib import Path

def export_csv(rows: list, file_path: str, fieldnames: list):
    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
