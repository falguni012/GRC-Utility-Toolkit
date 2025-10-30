# policy_tracker.py
"""
Compliance Policy Tracker
Tracks organization policies, owners, and review dates.
"""

import csv
from datetime import datetime

def add_policy(file, name, owner, review_date):
    with open(file, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([name, owner, review_date])
        print(f"✅ Policy '{name}' added successfully.")

def list_policies(file):
    try:
        with open(file, 'r') as csvfile:
            reader = csv.reader(csvfile)
            print("\n📋 Current Policies:\n------------------")
            for row in reader:
                name, owner, date = row
                status = "🔴 Overdue" if datetime.strptime(date, "%Y-%m-%d") < datetime.now() else "🟢 Active"
                print(f"{name} | {owner} | {date} | {status}")
    except FileNotFoundError:
        print("⚠️ No policies found.")

if __name__ == "__main__":
    file = "policies.csv"
    print("Compliance Policy Tracker")
    print("1. Add Policy\n2. List Policies")
    choice = input("Enter choice: ")
    if choice == "1":
        name = input("Policy Name: ")
        owner = input("Owner: ")
        review_date = input("Review Date (YYYY-MM-DD): ")
        add_policy(file, name, owner, review_date)
    elif choice == "2":
        list_policies(file)
