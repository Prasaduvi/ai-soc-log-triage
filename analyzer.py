import time

def analyze_logs(file_path, output_report):
    print("[*] Scanning logs for potential threats...\n")
    try:
        with open(file_path, 'r') as file, open(output_report, 'w') as report:
            
            report.write("=== AI SOC AUTOMATED INCIDENT REPORT ===\n\n")
            
            for line in file:
                if "Failed password" in line or "invalid user" in line:
                    alert_msg = f"[!] ALERT: Suspicious Activity Detected!\n    Log Details: {line.strip()}\n    Action: Recommended to block source IP.\n\n"
                    
                    print(alert_msg)
                    
                    report.write(alert_msg)
                    
                else:
                    print(f"[-] Normal: {line.strip()}")
                
                time.sleep(0.5)
                
        print(f"[*] Scanning complete! Alerts successfully saved to '{output_report}'.")
        
    except FileNotFoundError:
        print("[-] Error: Log file not found!")

if __name__ == "__main__":
    analyze_logs("sample_auth.log", "alert_report.txt")