from faker import Faker
import pandas as pd
import random

fake = Faker('en_IN')
data = {
    "Data Type": [fake.random_element(["Name", "Email", "Aadhaar (XXXX-XXXX-1234)", "Medical History"]) for _ in range(100)],
    "Data Source": [fake.random_element(["User Input Form", "Website Signup", "Third-Party API"]) for _ in range(100)],
    "Purpose of Processing": [fake.random_element(["Customer Onboarding", "KYC Verification", "Marketing Campaigns"]) for _ in range(100)],
    "Data Subject": [fake.random_element(["Customer", "Employee", "Vendor"]) for _ in range(100)],
    "Lawful Basis for Processing": [fake.random_element(["Consent", "Contract", "Legal Obligation"]) for _ in range(100)],
    "Consent Mechanism": [f"{fake.random_element(['Checkbox on Website', 'Digital Log', 'Mobile App Toggle'])} ({fake.date_time_this_year()})" for _ in range(100)],
    "Data Retention Period": [f"{random.randint(1, 5)} years post-termination" for _ in range(100)],
    "Storage Location": [fake.random_element(["AWS Mumbai", "Local DB", "Azure India"]) for _ in range(100)],
    "Access Controls": [fake.random_element(["HR Team", "DevOps (restricted)", "Compliance Officer"]) for _ in range(100)],
    "Third-party Sharing": [fake.random_element(["Payment Gateway", "CRM Provider", "Analytics Vendor"]) for _ in range(100)],
    "Cross-border Transfer": [fake.random_element(["No", "Yes, for analytics in Singapore"]) for _ in range(100)],
    "Children’s Data": [f"Yes, with parental consent (age {random.randint(5, 12)})" if random.choice([True, False]) else "No" for _ in range(100)],
    "Sensitive Personal Data": [fake.random_element(["Health", "Biometrics", "Financial"]) for _ in range(100)],
    "Data Breach Readiness": [fake.random_element(["Incident Response Policy", "72-hr alert", "Automated Detection Log"]) for _ in range(100)],
    "Data Minimization Check": [f"Yes, excess fields eliminated ({fake.word()})" if random.choice([True, False]) else "No, review pending" for _ in range(100)],
    "Data Rights Enabled": [fake.random_element(["Data Access Request Portal", "Correction Form", "Deletion Request"]) for _ in range(100)],
    "Retention & Deletion Policy": [f"Scheduled via backend cron job ({fake.date_time_this_decade()})" for _ in range(100)],
    "Audit Trails": [f"Yes, tracked with timestamp/user ({fake.date_time_this_year()}/user{random.randint(1, 100)})" for _ in range(100)],
    "Data Protection Officer": [f"{fake.name()}, dpo@clearconsent.in" for _ in range(100)],
    "Legal Basis Documentation": ["Section 4(1), DPDP Act compliance doc" for _ in range(100)]
}

df = pd.DataFrame(data)
df.to_csv("synthetic_consent_data_india.csv", index=False)
print("Synthetic data generated and saved to synthetic_consent_data_india.csv")
