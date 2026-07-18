from extractor import *


def parse_resume(file_name):

    with open(file_name, "r") as file:
        text = file.read()

    print("\nResume Details")
    print("-" * 40)

    print("Name :", extract_name(text))
    print("Email :", extract_email(text))
    print("Phone :", extract_phone(text))

    print("Skills :", extract_skills(text))
    print("Education :", extract_education(text))