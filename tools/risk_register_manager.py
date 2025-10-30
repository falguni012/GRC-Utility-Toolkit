# tools/risk_register_manager.py
import csv
import os

FILE = "risk_register.csv"

def add_risk():
    risk = input("Enter Risk Description: ")
    severity = input("Enter Severity (Low/Medium/High): ")
    impact = input("Enter Impact (Low/Medium/High): ")
    with open(FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([risk, severity, impact])
    print("✅ Risk added successfully!")

def list_risks():
    if not os.path.exists(FILE):
        print("📂 No risk register found.")
        return
    with open(FILE, 'r') as f:
        reader = csv.reader(f)
        print("\n📋 Current Risks:")
        for row in reader:
            print(f"- {row[0]} | Severity: {row[1]} | Impact: {row[2]}")

if __name__ == "__main__":
    print("1️⃣ Add Risk\n2️⃣ List Risks")
    choice = input("Select: ")
    if choice == "1":
        add_risk()
    else:
        list_risks()
