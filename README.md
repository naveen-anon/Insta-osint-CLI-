# Insta-OSINT CLI

![Python](https://img.shields.io/badge/Python-3.x-blue)
![OSINT](https://img.shields.io/badge/OSINT-Cyber%20Intelligence-red)
![Platform](https://img.shields.io/badge/Platform-Linux-green)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-Educational-yellow)

Professional Instagram OSINT and cyber intelligence toolkit built with Python.

---

## Features

✅ Public Profile Detection  
✅ Metadata Extraction  
✅ Followers / Following / Posts Parser  
✅ Username Intelligence  
✅ Keyword Analysis  
✅ Intelligence Scoring  
✅ JSON Report Export  
✅ Colorful Terminal Dashboard  

---

## Installation

Clone repository:

```bash
git clone https://github.com/naveen-anon/Insta-osint-CLI-.git
```

Move into project:

```bash
cd Insta-osint-CLI-
```

Install dependencies:

```bash
pip3 install -r requirements.txt
```

---

## Usage

Basic scan:

```bash
python3 main.py username
```

Full intelligence scan:

```bash
python3 main.py username --metadata --links --export json
```

Example:

```bash
python3 main.py <username> --metadata --links --export json
```

---

## Project Structure

```bash
Insta-osint-CLI-/
├── main.py
├── requirements.txt
│
├── core/
│   ├── banner.py
│   ├── cli.py
│   ├── logger.py
│
├── modules/
│   ├── profile_lookup.py
│   ├── metadata_parser.py
│   ├── profile_stats.py
│   ├── link_extractor.py
│   ├── username_intel.py
│   ├── keyword_analyzer.py
│   ├── score_engine.py
│   ├── display.py
│   ├── report_generator.py
│
└── output/
```

---

## Output Example

```text
Username     : cyber_defance_
Reachable    : True
Followers    : 19
Following    : 12
Posts        : 1
Intel Score  : 00
```

---

## Use Cases

- Public OSINT research
- Social media reconnaissance
- Username intelligence
- Cyber investigation workflows

---

## Disclaimer

This tool is designed only for:

- Publicly available information
- Authorized security research
- Educational purposes

Private account access, credential abuse, or privacy violations are not supported.

---

## Author

Naveen | Cyber Recon Hub
