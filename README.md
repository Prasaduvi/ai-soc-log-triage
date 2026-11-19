# AI-Assisted SOC Log Triage & Incident Summarizer

## Overview
A lightweight Python automation prototype designed for Security Operations Center (SOC) workflows. It continuously monitors authentication logs, filters out routine normal traffic, detects suspicious activities (such as brute-force attempts or invalid user logins), and generates automated incident alert reports.

## Key Features
- **Automated Log Parsing:** Reads and scans server authentication logs line-by-line.
- **Threat Detection:** Identifies patterns like `Failed password` and `invalid user`.
- **Alert Reporting:** Displays real-time alerts on the console and saves structured findings into `alert_report.txt`.
- **Future Scope:** Designed to integrate with SIEM tools (such as Splunk via REST API) and LLM APIs for automated threat summarization.

## Files Included
- `analyzer.py` — Main Python log analysis and alerting script.
- `sample_auth.log` — Sample log dataset for testing.
- `alert_report.txt` — Generated incident alert report.

## How to Run
1. Clone or download this repository.
2. Open terminal/CMD in the project folder.
3. Run the script:
   ```bash
   python analyzer.py
