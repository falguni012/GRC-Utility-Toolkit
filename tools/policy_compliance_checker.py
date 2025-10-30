MANDATORY_KEYWORDS = [
    "confidentiality",
    "integrity",
    "availability",
    "risk",
    "security",
    "incident response",
    "data protection"
]

def check_policy_compliance(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read().lower()

        found = [word for word in MANDATORY_KEYWORDS if word in content]
        missing = [word for word in MANDATORY_KEYWORDS if word not in content]
        compliance_score = (len(found) / len(MANDATORY_KEYWORDS)) * 100

        print(f"\n🔍 Compliance Report for: {file_path}")
        print(f"✅ Found Keywords: {found}")
        print(f"❌ Missing Keywords: {missing}")
        print(f"📊 Compliance Score: {compliance_score:.2f}%")

    except FileNotFoundError:
        print("❌ File not found. Please check your path.")

if __name__ == "__main__":
    path = input("Enter policy file path: ")
    check_policy_compliance(path)
