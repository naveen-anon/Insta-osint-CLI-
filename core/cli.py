import argparse


def create_parser():
    parser = argparse.ArgumentParser(
        prog="insta-osint",
        description="Instagram OSINT CLI Toolkit"
    )

    parser.add_argument(
        "targets",
        nargs="*",
        help="Instagram usernames"
    )

    parser.add_argument(
        "--export",
        choices=["json", "txt"],
        default="json",
        help="Export format"
    )

    parser.add_argument(
        "--batch",
        help="Load usernames from file"
    )

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose output"
    )

    parser.add_argument(
        "--links",
        action="store_true",
        help="Extract public links"
    )

    parser.add_argument(
        "--metadata",
        action="store_true",
        help="Parse metadata"
    )

    return parser
