import typer
from rich.console import Console
from collectors.profile import scan_profile

app = typer.Typer()
console = Console()

@app.command()
def profile(username: str):
    """
    Scan public Instagram profile metadata
    """
    result = scan_profile(username)

    if result:
        console.print(result)
