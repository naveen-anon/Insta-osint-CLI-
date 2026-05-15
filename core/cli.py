# core/cli.py
import argparse
from .logger import logger
from .banner import print_banner

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Insta-OSINT CLI – gather public Instagram intel"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Profile sub‑command
    sp_profile = subparsers.add_parser("profile", help="Collect public profile metadata")
    sp_profile.add_argument("username", help="Target Instagram username")
    sp_profile.add_argument("--output", "-o", help="Output file (JSON)", default=None)

    # Media sub‑command
    sp_media = subparsers.add_parser("media", help="Collect media metadata")
    sp_media.add_argument("username", help="Target Instagram username")
    sp_media.add_argument("--limit", type=int, default=20, help="Maximum posts to fetch")

    # Export sub‑command
    sp_export = subparsers.add_parser("export", help="Export collected data to CSV/JSON")
    sp_export.add_argument("format", choices=["json", "csv"], help="Export format")
    sp_export.add_argument("file", help="Destination file")

    return parser

def main():
    print_banner()
    parser = build_parser()
    args = parser.parse_args()

    # Dispatch
    if args.command == "profile":
        from collectors.profile import collect_profile
        data = collect_profile(args.username)
        if args.output:
            safe_write(args.output, json.dumps(data, indent=4))
        else:
            logger.info(json.dumps(data, indent=4))
    elif args.command == "media":
        from collectors.media import collect_media
        posts = collect_media(args.username, limit=args.limit)
        logger.info(f"Fetched {len(posts)} posts")
    elif args.command == "export":
        logger.info("Exporting not implemented yet – extend the exporter modules.")

if __name__ == "__main__":
    main()
