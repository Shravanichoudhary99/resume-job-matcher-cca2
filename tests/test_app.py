import sys
from io import BytesIO
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import app as app_module  # noqa: E402


def test_health():
    client = app_module.app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_skills_api():
    client = app_module.app.test_client()

    response = client.post(
        "/api/skills",
        json={"text": "Python Flask Docker Git"}
    )

    assert response.status_code == 200

    data = response.get_json()

    assert "skills" in data
    assert "Python" in data["skills"]["Programming"]
    assert "Flask" in data["skills"]["Frameworks and Libraries"]


def test_skills_api_empty_input():
    client = app_module.app.test_client()

    response = client.post(
        "/api/skills",
        json={"text": "   "}
    )

    assert response.status_code == 400


def test_invalid_resume():
    client = app_module.app.test_client()

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


def test_adding_data(tmp_path, monkeypatch):
    data_file = tmp_path / "analyses.json"

    monkeypatch.setattr(
        app_module,
        "DATA_FILE",
        str(data_file)
    )

    monkeypatch.setattr(
        app_module,
        "extract_text_from_pdf",
        lambda _: "Python Flask Docker"
    )

    client = app_module.app.test_client()

    response = client.post(
        "/compare",
        data={
            "resume": (
                BytesIO(b"fake pdf"),
                "resume.pdf"
            ),
            "job1_title": "Python Developer",
            "job1": "Python Flask Docker"
        },
        content_type="multipart/form-data"
    )

    assert response.status_code == 200

    saved = app_module.load_analyses()

    assert len(saved) == 1
    assert saved[0]["resume_filename"] == "resume.pdf"
    assert len(saved[0]["jobs"]) == 1
    assert saved[0]["jobs"][0]["match_percentage"] == 100.0
