
def classify_incident(text):
    text = text.lower()

    categories = {
        "Phishing": ["phishing", "email", "fake link", "attachment", "credential"],
        "Unpatched Vulnerability": ["unpatched", "outdated", "vulnerability", "exploit", "patch"],
        "Misconfiguration": ["misconfiguration", "open port", "public access", "incorrect settings"],
        "Insider Threat": ["insider", "employee", "staff", "unauthorized access", "data theft"],
        "Supply-Chain Compromise": ["supply chain", "vendor", "third party", "software update", "supplier"]
    }

    scores = {}

    for category, keywords in categories.items():
        scores[category] = sum(
            1 for word in keywords if word in text
        )

    result = max(scores, key=scores.get)

    if scores[result] == 0:
        return "Unknown Root Cause"

    return result


incident = input("Enter security incident description: ")

result = classify_incident(incident)

print("\n--- Security Incident Analysis ---")
print("Incident:", incident)
print("Root Cause Category:", result)
