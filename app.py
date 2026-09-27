from flask import Flask, render_template, request

from services.pdf_extractor import extract_text_from_pdf

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    resume = request.files.get("resume")
    job_description = request.form.get("job_description")

    if not resume:
        return "Resume is required", 400

    if not job_description:
        return "Job description is required", 400

    resume_text = extract_text_from_pdf(resume)

    if not resume_text:
        return "Could not extract text from the PDF", 400

    return (
        f"Resume received: {resume.filename}<br><br>"
        f"Extracted text:<br><pre>{resume_text}</pre>"
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )