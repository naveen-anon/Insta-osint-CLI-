# Insta‑OSINT CLI

A lightweight Python CLI for gathering public Instagram intelligence.

## Features
- Public profile metadata
- Recent media (photos / reels)
- Basic timeline analysis
- JSON / CSV / HTML export
- Simple SQLite persistence

## Installation

```bash
git clone https://github.com/yourname/insta-osint-cli.git
cd insta-osint-cli
pip install -r requirements.txt
```
## usage 
``
python main.py profile natgeo
python main.py media natgeo --limit 50
python main.py export json output.json
``
