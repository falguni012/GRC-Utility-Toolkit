# tools/vendor_risk_evaluator.py

QUESTIONS = [
    "Does the vendor have a security policy?",
    "Do they conduct regular penetration testing?",
    "Is data encrypted at rest and in transit?",
    "Do they provide breach notifications?",
    "Is there an NDA in place?"
]

def vendor_eval():
    score = 0
    for q in QUESTIONS:
        ans = input(f"{q} (yes/no): ").lower()
        if ans == "yes":
            score += 1

    risk = "Low" if score >= 4 else "Medium" if score >= 2 else "High"
    print(f"\n📊 Vendor Risk Score: {score}/5")
    print(f"⚠️ Overall Vendor Risk: {risk}")

if __name__ == "__main__":
    vendor_eval()
