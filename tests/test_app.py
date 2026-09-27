import sys
from io import BytesIO
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app import app


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_skills_api():
    client = app.test_client()

    response = client.post(
        "/api/skills",
        json={
            "text": "Python Flask Docker Git"
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert "skills" in data
    assert "Python" in data["skills"]["Programming"]
    assert "Flask" in data["skills"]["Frameworks and Libraries"]


def test_skills_api_empty_input():
    client = app.test_client()

    response = client.post(
        "/api/skills",
        json={
            "text": "   "
        }
    )

    assert response.status_code == 400


def test_invalid_resume():
    client = app.test_client()

    response = client.post(
        "/compare",
        data={
            "resume": (
                BytesIO(b"not a pdf file"),
                "resume.txt"
            )
        },
        content_type="multipart/form-data"
    )

    assert response.status_code == 400
    assert response.get_data(as_text=True) == (
        "Only PDF files are allowed"
    )