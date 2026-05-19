# Insta-OSINT CLI

![Python](https://img.shields.io/badge/Python-3.x-blue)
![OSINT](https://img.shields.io/badge/OSINT-Cyber%20Intelligence-red)
![Platform](https://img.shields.io/badge/Platform-Linux-green)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-yellow)

Professional Instagram OSINT & Cyber Intelligence Toolkit built with Python.

---

## Community

[![WhatsApp](https://img.shields.io/badge/WhatsApp-Channel-25D366?logo=whatsapp&logoColor=white)](https://whatsapp.com/channel/0029Vb6o1ejAjPXQi2KCAk1f)

[![Telegram](https://img.shields.io/badge/Telegram-Channel-26A5E4?logo=telegram&logoColor=white)](https://t.me/cyber_recon_hub)

[![Discord](https://img.shields.io/badge/Discord-Server-5865F2?logo=discord&logoColor=white)](https://discord.gg/XJQmx3XP8)

---

## Features

✅ Public / Private Account Detection  
✅ Verified Badge Detection  
✅ Business Account Detection  
✅ Creator Account Detection  
✅ Followers / Following / Posts Parser  
✅ Instagram Bio Extraction  
✅ Metadata Intelligence  
✅ Username Intelligence  
✅ Keyword Analysis  
✅ Intelligence Scoring System  
✅ JSON Report Export  
✅ Rich Terminal Dashboard  
✅ Link Extraction Engine  

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

Basic Scan:

```bash
python3 main.py username
```

Metadata Scan:

```bash
python3 main.py username --metadata
```

Full Intelligence Scan:

```bash
python3 main.py username --metadata --links --export json
```

Example:

```bash
python3 main.py cyber_defance_ --metadata --links --export json
```

---

## Output Example

```text
┌──(root㉿localhost)-[/home/kali/Insta-osint-CLI-]
└─# python3 main.py cyber_defance_ --metadata --verbose --links --export json
╭───── Cyber Intelligence Suite ──────╮
│ CYBER INTELLIGENCE CLI              │
│ OSINT • Recon • Threat Intelligence │
╰─────────────────────────────────────╯
[INFO] Scanning cyber_defance_
[✓] Intelligence Scan Complete
           Instagram Intelligence Report
┏━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Field       ┃ Value                              ┃
┡━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Username    │ cyber_defance_                     │
│ Reachable   │ True                               │
│ Followers   │ 18                                 │
│ Following   │ 14                                 │
│ Posts       │ 1                                  │
│ Bio         │ 🛡️ Cyber Defense | Ethical Security │
│             │ 💻 Code • Protect • Repeat         │
│             │ 🔐 Privacy is Power                │
│             │ ⚡ Securing the Digital World      │
│ Private     │ False                              │
│ Verified    │ False                              │
│ Business    │ True                               │
│ Intel Score │ 75                                 │
└─────────────┴────────────────────────────────────┘
```

---

## Screenshots

## Metadata Intelligence Scan

![Demo 1](assets/Screenshot_2026-05-19-10-38-59-02_84d3000e3f4017145260f7618db1d683.jpg)

---

## Full Intelligence Report

![Demo 2](assets/IMG_20260519_102630.jpg)

---

## Project Structure

```bash
Insta-osint-CLI-/
│
├── main.py
├── requirements.txt
├── LICENSE
├── README.md
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
│   ├── account_analyzer.py
│   ├── link_extractor.py
│   ├── username_intel.py
│   ├── keyword_analyzer.py
│   ├── score_engine.py
│   ├── display.py
│   ├── report_generator.py
│
├── assets/
│   ├── demo1.jpg
│   ├── demo2.jpg
│
└── output/
    └── reports/
```

---

## Tech Stack

- Python
- Requests
- BeautifulSoup4
- Rich

---

## Use Cases

- Public OSINT Research
- Instagram Reconnaissance
- Cyber Intelligence
- Username Intelligence
- Threat Investigation Workflows

---

## Disclaimer

This tool is designed only for:

- Publicly available information
- Authorized security research
- Educational purposes

Private account access, credential abuse, or privacy violations are not supported.

---

## License

This project is licensed under the MIT License.

---

## Author

Naveen | Cyber Recon Hub
