

import argparse

def create_parser(): parser = argparse.ArgumentParser( prog="insta-osint", description="Instagram public OSINT toolkit" )

sub = parser.add_subparsers(dest="command")

lookup = sub.add_parser("lookup", help="Lookup public profile")
lookup.add_argument("username", help="Instagram username")

export = sub.add_parser("export", help="Export profile to JSON")
export.add_argument("username", help="Instagram username")

check = sub.add_parser("check", help="Check username availability")
check.add_argument("username", help="Instagram username")

return parser


