# exports/json_export.py
def export_json(data: dict, file_path: str):
    from pathlib import Path
    Path(file_path).write_text(json.dumps(data, indent=4), encoding="utf-8")
