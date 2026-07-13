from flask import Flask, render_template, request, jsonify, session
from pdf_reader import extract_text
from ocr_reader import extract_text_from_image
from gemini_service import analyze_report
from chatbot import chat_with_report
import os

app = Flask(__name__)

# Secret key for Flask session
# app.secret_key = "sehat_vault_secret_key"
app.secret_key = os.getenv("SECRET_KEY", "sehat_vault_secret_key")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    if "report" not in request.files:
        return "No file uploaded"

    file = request.files["report"]

    if file.filename == "":
        return "No file selected"

    os.makedirs("uploads", exist_ok=True)

    filepath = os.path.join("uploads", file.filename)
    file.save(filepath)

    filename = file.filename.lower()

    if filename.endswith(".pdf"):
        extracted_text = extract_text(filepath)

    elif filename.endswith((".jpg", ".jpeg", ".png")):
        extracted_text = extract_text_from_image(filepath)

    else:
        return "Unsupported File Format"

    # Store report in session
    session["report_text"] = extracted_text

    # Reset previous conversation
    session["chat_history"] = []

    ai_result = analyze_report(extracted_text)

    return render_template(
        "result.html",
        summary=ai_result["summary"],
        findings=ai_result["abnormal_findings"],
        diseases=ai_result["possible_diseases"],
        recommendations=ai_result["recommendations"],
    )


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    if not data:
        return jsonify({"reply": "Invalid request."})

    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"reply": "Please type a message."})

    report_text = session.get("report_text")

    if not report_text:
        return jsonify({
            "reply": "Please upload and analyze a medical report first."
        })

    history = session.get("chat_history", [])

    reply = chat_with_report(
        report_text,
        history,
        user_message
    )

    history.append({
        "user": user_message,
        "assistant": reply
    })

    session["chat_history"] = history

    return jsonify({
        "reply": reply
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)