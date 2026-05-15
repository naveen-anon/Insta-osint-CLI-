# exports/html_report.py
def export_html(data: dict, file_path: str):
    # Very simple HTML rendering – replace with Jinja2 if needed
    html = "<html><body>"
    for key, val in data.items():
        html += f"<h2>{key}</h2><pre>{val}</pre>"
    html += "</body></html>"
    Path(file_path).write_text(html, encoding="utf-8")
