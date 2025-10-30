# tools/compliance_maturity_scorer.py

DOMAINS = ["Access Control", "Incident Response", "Data Security", "Training", "Monitoring"]

def maturity_scorer():
    print("📊 Enter maturity level (1–5) for each domain:\n")
    total = 0
    for d in DOMAINS:
        score = int(input(f"{d}: "))
        total += score

    avg = total / len(DOMAINS)
    if avg < 2:
        level = "Initial"
    elif avg < 3.5:
        level = "Managed"
    else:
        level = "Optimized"

    print(f"\n✅ Average Score: {avg:.2f}")
    print(f"🏆 Maturity Level: {level}")

if __name__ == "__main__":
    maturity_scorer()
