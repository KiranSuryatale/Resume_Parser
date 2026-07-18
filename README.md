# Resume Parser

A beginner-friendly, modular NLP application designed to extract key entities from resume text files. It uses Regular Expressions (Regex) and basic string processing to identify and parse contact information, skills, and educational qualifications automatically.

## 🚀 Features
- **Automated Extraction:** Effortlessly retrieves Name, Email, and Phone number using Regex patterns.

- **Skill Matching:** Searches for predefined technical skills within the resume text.

- **Education Parsing:** Identifies educational qualifications based on a keyword list.

- **Modular Design:** Cleanly separated logic for extraction, parsing, and execution.

- **Interactive UI:** A simple CLI (Command Line Interface) to input and process files.
## 📂 Project Structure
```text
Resume_Parser/
│
├── main.py              # Application entry point and menu
├── parser.py            # Handles file reading and orchestration
├── extractor.py         # Core logic using Regex and string matching
├── sample_resume.txt    # Sample resume file for testing
├── requirements.txt     # List of project dependencies
├── .gitignore
└── README.md            # Project documentation
