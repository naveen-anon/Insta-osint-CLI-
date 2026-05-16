File: main.py

import argparse from core.banner import show_banner from modules.profile_lookup import fetch_public_profile from modules.export import export_json

def main(): parser = argparse.ArgumentParser(prog="insta-osint") sub = parser.add_subparsers(dest="command")

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

if name == "main": main()

File: core/banner.py

def show_banner(): print("=" * 40) print("INSTA OSINT CLI") print("Public profile research tool") print("=" * 40)

File: modules/profile_lookup.py

import requests

def fetch_public_profile(username: str): url = f"https://www.instagram.com/{username}/" headers = { "User-Agent": "Mozilla/5.0" }

r = requests.get(url, headers=headers, timeout=15)

return {
    "username": username,
    "status_code": r.status_code,
    "profile_url": url,
    "reachable": r.ok
}

File: modules/export.py

import json import os

def export_json(username, data): os.makedirs("output/json", exist_ok=True)

path = f"output/json/{username}.json"

with open(path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

return path

File: requirements.txt

requests
