# Insta-OSINT CLI

Professional Instagram OSINT and Cyber Intelligence toolkit built with Python.

---

## Features

### Intelligence Modules

- Username Intelligence
- Profile Metadata Analysis
- Public Link Extraction
- Keyword Intelligence
- JSON Intelligence Reports
- Colorful CLI Interface

---

## Installation

### Clone Repository

```bash
git clone https://github.com/naveen-anon/insta_osint.git
```

### Enter Project Directory

```bash
cd insta_osint
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

### Basic Scan

```bash
python3 main.py cyber_defence_
```

### Generate Intelligence Report

```bash
python3 main.py cyber_defence_ --export json
```

### Batch Scan

```bash
python3 main.py --batch usernames.txt
```

---

## Project Structure

```bash
insta-osint-cli/
├── main.py
├── requirements.txt
├── config.yaml
│
├── core/
│   ├── cli.py
│   ├── banner.py
│   ├── logger.py
│
├── modules/
│   ├── profile_lookup.py
│   ├── metadata_parser.py
│   ├── link_extractor.py
│   ├── username_intel.py
│   ├── keyword_analyzer.py
│   ├── report_generator.py
│
├── output/
│   ├── json/
│   ├── reports/
│
└── docs/
```

---

## Modules

### profile_lookup.py
Fetches public profile data.

### metadata_parser.py
Extracts metadata from profile.

### link_extractor.py
Extracts public links.

### username_intel.py
Analyzes username patterns.

### keyword_analyzer.py
Analyzes public keywords.

### report_generator.py
Creates timestamped intelligence reports.

---

## Output

Reports are saved inside:

```bash
output/reports/
```

Example:

```bash
cyber_defence__20260518_010203.json
```

---

## Tech Stack

- Python
- Requests
- Rich

---

## Use Cases

- Public OSINT Research
- Username Intelligence
- Social Media Reconnaissance
- Cyber Intelligence Workflows

---

## Disclaimer

This project is designed only for:

- Publicly available information
- Authorized security research
- Educational purposes

Private account access, credential abuse, or privacy violations are not supported.

---

## Author

Built by Naveen | Cyber Recon Hub
