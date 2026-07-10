from flask import Flask, render_template, request
from pdf_reader import extract_text
from ocr_reader import extract_text_from_image
from gemini_service import analyze_report
import os

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["report"]
    filepath = os.path.join("uploads", file.filename)

    # Save uploaded file
    file.save(filepath)

    # Check file type
    filename = file.filename.lower()

    if filename.endswith(".pdf"):
        extracted_text = extract_text(filepath)

    elif filename.endswith((".jpg", ".jpeg", ".png")):
        extracted_text = extract_text_from_image(filepath)

    else:
        return "Unsupported File Format"

    # Send extracted text to Gemini
    ai_result = analyze_report(extracted_text)

    return render_template(
    "result.html",
    summary=ai_result["summary"],
    findings=ai_result["abnormal_findings"],
    diseases=ai_result["possible_diseases"],
    recommendations=ai_result["recommendations"])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)