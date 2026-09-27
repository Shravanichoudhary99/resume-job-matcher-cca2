from flask import Flask, render_template, request

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

    return (
        f"Resume received: {resume.filename}<br>"
        f"Job description received successfully."
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )