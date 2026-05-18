from rich import print

from core.cli import create_parser
from core.banner import show_banner
from core.logger import setup_logger

from modules.profile_lookup import fetch_public_profile
from modules.metadata_parser import parse_metadata
from modules.link_extractor import extract_links

from modules.profile_stats import extract_profile_stats

from modules.username_intel import analyze_username
from modules.keyword_analyzer import analyze_keywords
from modules.report_generator import generate_report
from modules.score_engine import calculate_score

logger = setup_logger()


def main():

    parser = create_parser()

    args = parser.parse_args()

    show_banner()

    if not args.targets:

        parser.print_help()

        return

    username = args.targets[0]

    logger.info(
        f"Scanning {username}"
    )

    profile_data = fetch_public_profile(
        username
    )

    metadata = parse_metadata(
        profile_data
    )

    stats = extract_profile_stats(
        metadata
    ) stats = extract_profile_stats(
        metadata
    )

    bio_text = metadata.get(
        "description",
        ""
    )

    links = []

    if args.links:

        links = extract_links(
            profile_data.get(
                "html_content",
                ""
            )
        )

    score_data = calculate_score(
        bio_text,
        len(links)
    )

    final_data = {
        "profile": {
            "username": profile_data.get(
                "username"
            ),
            "status_code": profile_data.get(
                "status_code"
            ),
            "profile_url": profile_data.get(
                "profile_url"
            ),
            "reachable": profile_data.get(
                "reachable"
            )
        }
    }

    if args.metadata:

        final_data[
            "metadata"
        ] = metadata

    final_data[
        "profile_stats"
    ] = stats

    if args.links:

        final_data[
            "links"
        ] = links

    final_data[
        "username_intelligence"
    ] = analyze_username(
        username
    )

    final_data[
        "keyword_analysis"
    ] = analyze_keywords(
        bio_text
    )

    final_data[
        "intelligence_score"
    ] = score_data

    print(
        "[bold green][✓] Intelligence Scan Complete[/bold green]"
    )

    print(
        final_data
    )

    if args.export:

        report_path = generate_report(
            username,
            final_data
        )

        print(
            f"[cyan][+] Report saved:[/cyan] {report_path}"
        )


if __name__ == "__main__":
    main()
