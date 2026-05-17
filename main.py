from rich import print

from core.cli import create_parser
from core.banner import show_banner
from core.logger import setup_logger

from modules.profile_lookup import fetch_public_profile
from modules.metadata_parser import parse_metadata
from modules.link_extractor import extract_links

from modules.username_intel import analyze_username
from modules.keyword_analyzer import analyze_keywords
from modules.report_generator import generate_report

logger = setup_logger()


def main():
    parser = create_parser()
    args = parser.parse_args()

    show_banner()

    if not args.targets:
        parser.print_help()
        return

    username = args.targets[0]

    logger.info(f"Scanning {username}")

    profile_data = fetch_public_profile(username)

    metadata = parse_metadata(profile_data)

    links = extract_links(str(profile_data))

    username_analysis = analyze_username(username)

    keyword_analysis = analyze_keywords(str(profile_data))

    final_data = {
        "profile": profile_data,
        "metadata": metadata,
        "links": links,
        "username_intelligence": username_analysis,
        "keyword_analysis": keyword_analysis
    }

    print("[bold green][✓] Intelligence Scan Complete[/bold green]")
    print(final_data)

    if args.export:
        report_path = generate_report(username, final_data)
        print(f"[cyan][+] Report saved:[/cyan] {report_path}")


if __name__ == "__main__":
    main()
