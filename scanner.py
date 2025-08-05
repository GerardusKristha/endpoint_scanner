import os
from datetime import datetime

# Konfigurasi
SCAN_PATH = "E:\Project\endpoint_scanner\suspicious_folder"
SUSPICIOUS_EXT = ['.exe', '.bat', '.vbs', '.js', '.scr']
LOG_FILE = "E:\Project\endpoint_scanner\suspicious.log"

# Fungsi untuk mencatat ke log file
def write_log(message):
    with open(LOG_FILE, "a", encoding="utf-8") as log:
        log.write(f"[{datetime.now()}] {message}\n")

# Fungsi untuk scan file mencurigakan
def scan_files(path):
    print("🔍 Scanning for suspicious files...\n")
    for root, _, files in os.walk(path):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in SUSPICIOUS_EXT:
                full_path = os.path.join(root, file)
                alert = f"🚨 Suspicious file found: {full_path}"
                print(alert)
                write_log(alert)

# Program utama
if __name__ == "__main__":
    if not os.path.exists(SCAN_PATH):
        print(f"❌ Path '{SCAN_PATH}' not found.")
    else:
        scan_files(SCAN_PATH)
        print("\n✅ Scan completed. Check suspicious.log for results.")
