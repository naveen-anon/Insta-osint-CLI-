import argparse
from core.banner import show_banner
from modules.profile_lookup import fetch_public_profile
from modules.export import export_json


def main():
    parser = argparse.ArgumentParser(prog="insta-osint")
    sub = parser.add_subparsers(dest="command")

    lookup = sub.add_parser("lookup")
    lookup.add_argument("username")

    export = sub.add_parser("export")
    export.add_argument("username")

    args = parser.parse_args()

    show_banner()

    if args.command == "lookup":
        data = fetch_public_profile(args.username)
        print(data)

    elif args.command == "export":
        data = fetch_public_profile(args.username)
        path = export_json(args.username, data)
        print(f"Saved: {path}")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
  
