from datetime import datetime

readme_content = f"""# 🛡️ Endpoint Suspicious File Scanner

A simple Python tool to scan directories for potentially malicious files based on known dangerous extensions. This tool simulates basic endpoint protection behavior and generates a scan log for further review.

## 📁 Project Structure

endpoint_scanner/
├── scanner.py ← Main Python script
├── suspicious_folder/ ← Sample directory to scan
│ ├── harmless.txt
│ ├── autorun.bat
│ └── virus.exe
├── suspicious.log ← Auto-generated scan results
└── README.md ← Project documentation

markdown
Always show details

Copy code

## 🚀 Features

- Scans for suspicious file types: `.exe`, `.bat`, `.vbs`, `.js`, `.scr`
- Recursively walks through target directory
- Logs all findings with timestamps to a file (`suspicious.log`)
- Uses basic Python (no external libraries)

## ✅ How It Works

1. The script walks through a target folder.
2. It checks each file extension.
3. If a file is deemed suspicious, it is logged in the `suspicious.log` file with a timestamp.

## 🧪 How to Use

1. Clone or download this repository.
2. Put files to be scanned inside the `suspicious_folder/`.
3. Run the script using Python:

```bash
python scanner.py
Check the results in the terminal and in suspicious.log.

🔍 Sample Output
bash
Always show details

Copy code
🔍 Scanning for suspicious files...

🚨 Suspicious file found: suspicious_folder/virus.exe
🚨 Suspicious file found: suspicious_folder/autorun.bat

✅ Scan completed. Check suspicious.log for results.
🛠️ Technologies Used
Python 3

Built-in modules: os, datetime

📚 Learning Goals
This project demonstrates:

Basic endpoint security logic

How to handle file operations in Python

How to implement simple logging mechanisms

📄 License
This is an open educational project. Feel free to modify or extend it.

✍️ Author
Created by Gerardus Bayu – {datetime.today().strftime('%B %Y')}.
"""

readme_path = "/mnt/data/README.md"
with open(readme_path, "w", encoding="utf-8") as f:
f.write(readme_content)

readme_path