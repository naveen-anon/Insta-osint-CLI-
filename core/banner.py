from rich.console import Console
from rich.panel import Panel

console = Console()


def show_banner():
    console.print(
        Panel.fit(
            "[bold red]CYBER INTELLIGENCE CLI[/bold red]\n"
            "[cyan]OSINT • Recon • Threat Intelligence[/cyan]",
            title="[yellow]Cyber Intelligence Suite[/yellow]"
        )
    )
