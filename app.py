from flask import Flask, jsonify, render_template, request

from services.pdf_extractor import extract_text_from_pdf
from services.skill_extractor import extract_skills
from services.matcher import match_skills


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/api/skills", methods=["POST"])
def api_skills():
    data = request.get_json()

    if not data or not data.get("text", "").strip():
        return jsonify({"error": "Text is required"}), 400

    skills = extract_skills(data["text"])

    return jsonify({
        "skills": skills
    })


@app.route("/analyze", methods=["POST"])
def analyze():
    resume = request.files.get("resume")
    job_description = request.form.get(
        "job_description", ""
    ).strip()

    if not resume or not resume.filename:
        return "Resume is required", 400

    if not resume.filename.lower().endswith(".pdf"):
        return "Only PDF files are allowed", 400

    if not job_description:
        return "Job description is required", 400

    resume_text = extract_text_from_pdf(resume)

    if not resume_text:
        return "Could not extract text from the PDF", 400

    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)

    analysis = match_skills(resume_skills, job_skills)

    return render_template(
        "result.html",
        resume_filename=resume.filename,
        matched_skills=analysis["matched"],
        missing_skills=analysis["missing"],
        match_percentage=analysis["match_percentage"]
    )


@app.route("/compare", methods=["POST"])
def compare():
    resume = request.files.get("resume")

    if not resume or not resume.filename:
        return "Resume is required", 400

    if not resume.filename.lower().endswith(".pdf"):
        return "Only PDF files are allowed", 400

    resume_text = extract_text_from_pdf(resume)

    if not resume_text:
        return "Could not extract text from the PDF", 400

    resume_skills = extract_skills(resume_text)

    results = []

    for i in range(1, 4):
        job_title = request.form.get(
            f"job{i}_title", ""
        ).strip()

        job_description = request.form.get(
            f"job{i}", ""
        ).strip()

        if not job_description:
            continue

        job_skills = extract_skills(job_description)

        analysis = match_skills(
            resume_skills,
            job_skills
        )

        results.append({
            "title": job_title or f"Job {i}",
            "match_percentage": analysis["match_percentage"],
            "matched_skills": analysis["matched"],
            "missing_skills": analysis["missing"]
        })

    if not results:
        return "Please enter at least one job description.", 400

    return render_template(
        "compare_result.html",
        resume_filename=resume.filename,
        results=results
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
