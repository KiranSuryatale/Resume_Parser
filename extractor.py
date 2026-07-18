import re


def extract_name(text):
    match = re.search(r"Name\s*:\s*(.*)", text)
    return match.group(1) if match else "Not Found"


def extract_email(text):
    match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+", text)
    return match.group() if match else "Not Found"


def extract_phone(text):
    match = re.search(r"\b\d{10}\b", text)
    return match.group() if match else "Not Found"


def extract_skills(text):

    skill_list = [
        "Python",
        "Pandas",
        "NumPy",
        "Machine Learning",
        "SQL",
        "Power BI",
        "Excel",
        "Java",
        "C++"
    ]

    found = []

    for skill in skill_list:
        if skill.lower() in text.lower():
            found.append(skill)

    return found


def extract_education(text):

    education = [
        "B.E.",
        "B.Tech",
        "M.Tech",
        "B.Sc",
        "M.Sc",
        "MBA"
    ]

    found = []

    for item in education:
        if item.lower() in text.lower():
            found.append(item)

    return found