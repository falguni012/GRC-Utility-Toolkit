# tools/compliance_report_generator.py

def generate_report():
    domains = {}
    while True:
        domain = input("Enter domain name (or 'done' to finish): ")
        if domain.lower() == "done":
            break
        score = int(input(f"Enter compliance score (0–100) for {domain}: "))
        domains[domain] = score

    avg = sum(domains.values()) / len(domains)
    with open("compliance_report.txt", "w") as f:
        f.write("📘 Compliance Summary Report\n")
        f.write("----------------------------\n")
        for k, v in domains.items():
            f.write(f"{k}: {v}%\n")
        f.write(f"\nOverall Compliance: {avg:.2f}%\n")

    print("\n✅ Report generated as 'compliance_report.txt'.")

if __name__ == "__main__":
    generate_report()
