import re


SKILL_CATEGORIES = {
    "Programming": [
        "Python",
        "Java",
        "JavaScript",
        "C",
        "C++",
        "C#",
        "PHP",
        "Ruby",
        "Go",
        "Kotlin",
        "Swift",
        "R",
        "TypeScript",
        "HTML",
        "CSS"
    ],

    "Frameworks and Libraries": [
        "Flask",
        "Django",
        "FastAPI",
        "React",
        "Angular",
        "Vue",
        "Node.js",
        "Express",
        "Spring",
        "Spring Boot",
        "Bootstrap",
        "jQuery",
        "TensorFlow",
        "PyTorch",
        "Scikit-learn",
        "Pandas",
        "NumPy"
    ],

    "Databases": [
        "SQL",
        "MySQL",
        "PostgreSQL",
        "SQLite",
        "MongoDB",
        "Oracle",
        "Redis",
        "Firebase",
        "DynamoDB"
    ],

    "Cloud and DevOps": [
        "Cloud Computing",
        "AWS",
        "Amazon Web Services",
        "Azure",
        "Microsoft Azure",
        "Google Cloud",
        "GCP",
        "Docker",
        "Kubernetes",
        "Git",
        "GitHub",
        "GitLab",
        "Jenkins",
        "CI/CD",
        "Continuous Integration",
        "Continuous Deployment",
        "Linux",
        "Terraform",
        "Ansible"
    ],

    "Data and AI": [
        "Machine Learning",
        "Deep Learning",
        "Artificial Intelligence",
        "Natural Language Processing",
        "NLP",
        "Computer Vision",
        "Data Science",
        "Data Analysis",
        "Data Analytics",
        "Pandas",
        "NumPy",
        "Matplotlib",
        "Seaborn",
        "Scikit-learn",
        "TensorFlow",
        "PyTorch"
    ],

    "Software Development": [
        "Software Development",
        "Object-Oriented Programming",
        "OOP",
        "Data Structures",
        "Algorithms",
        "REST API",
        "RESTful API",
        "API Development",
        "Microservices",
        "Unit Testing",
        "Integration Testing",
        "Debugging",
        "Version Control",
        "Agile",
        "Scrum"
    ],

    "Networking": [
        "Computer Networks",
        "TCP/IP",
        "HTTP",
        "HTTPS",
        "DNS",
        "VPN",
        "LAN",
        "WAN",
        "OSI Model",
        "Networking"
    ],

    "Tools and Platforms": [
        "VS Code",
        "Visual Studio",
        "Postman",
        "Jira",
        "GitHub Actions",
        "GitLab CI",
        "Microsoft Excel",
        "Power BI",
        "Tableau"
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