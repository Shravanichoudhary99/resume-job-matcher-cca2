import re


SKILL_CATEGORIES = {
    "Programming": [
        "Python",
        "Java",
        "JavaScript",
        "HTML",
        "CSS"
    ],
    "Frameworks": [
        "Flask",
        "React"
    ],
    "Databases": [
        "SQL"
    ],
    "Cloud and DevOps": [
        "AWS",
        "Docker",
        "Git"
    ],
    "Data and AI": [
        "Machine Learning",
        "Pandas",
        "NumPy"
    ]
}


def extract_skills(text):
    found_skills = {}

    for category, skills in SKILL_CATEGORIES.items():
        matched = []

        for skill in skills:
            pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"

            if re.search(pattern, text, re.IGNORECASE):
                matched.append(skill)

        if matched:
            found_skills[category] = matched

    return found_skills