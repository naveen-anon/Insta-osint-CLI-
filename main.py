import argparse
from rich import print

from core.banner import show_banner
from core.logger import setup_logger

from modules.profile_lookup import fetch_public_profile
from modules.username_check import username_exists
from modules.metadata_parser import parse_metadata
from modules.link_extractor import extract_links
from modules.export import export_json

logger = setup_logger()


def main():
    parser = argparse.ArgumentParser(prog="insta-osint")
    sub = parser.add_subparsers(dest="command")

    lookup = sub.add_parser("lookup")
    lookup.add_argument("username")

    export = sub.add_parser("export")
    export.add_argument("username")

    check = sub.add_parser("check")
    check.add_argument("username")

    args = parser.parse_args()

    show_banner()

    if args.command == "lookup":
        data = fetch_public_profile(args.username)
        meta = parse_metadata(data)
        links = extract_links(meta)

        print("[bold green][✓] Scan Complete[/bold green]")
        print({
            "profile": data,
            "metadata": meta,
            "links": links
        })

    elif args.command == "export":
        data = fetch_public_profile(args.username)
        path = export_json(args.username, data)

        print(f"[cyan][+] Exported:[/cyan] {path}")

    elif args.command == "check":
        exists = username_exists(args.username)

        if exists:
            print("[green][✓] Username exists[/green]")
        else:
            print("[red][✗] Username not found[/red]")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
