from rich.console import Console
from rich.panel import Panel

console = Console()


def show_banner():
    console.print(
        Panel.fit(
            "[bold cyan]INSTA OSINT CLI[/bold cyan]\n"
            "[green]Instagram Public Research Toolkit[/green]",
            title="[yellow]Cyber Recon Hub[/yellow]"
        )
    )
