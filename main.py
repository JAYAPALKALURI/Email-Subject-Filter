email_subjects = [
    "New Lead from Form",
    "Daily Report",
    "Zoom Invite",
    "Cybersecurity Lead"
]

for subject in email_subjects:
    if "lead" in subject.lower():
        print(subject)
