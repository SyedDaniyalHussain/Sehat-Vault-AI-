# 🩺 Sehat Vault AI

**Sehat Vault AI** is an intelligent medical report analyzer that helps users understand their lab reports and medical documents in simple, easy-to-understand language. Users can upload a medical report (PDF or image), and the app uses Google's Gemini AI to extract, analyze, and explain the findings — along with an interactive chatbot to ask follow-up questions about the report.

---

## ✨ Features

- 📄 **PDF & Image Upload** — Upload medical reports as PDF or image files (JPG, PNG)
- 🔍 **Text Extraction** — Extracts text from PDFs using PyMuPDF and from images using OCR (EasyOCR)
- 🤖 **AI-Powered Analysis** — Uses Google Gemini AI to generate:
  - A simple summary of the report
  - Abnormal findings
  - Possible diseases/conditions
  - Recommendations
- 💬 **Interactive Chatbot** — Ask questions about your uploaded report and get context-aware answers
- 🔒 **Session-Based Privacy** — Each user's report and chat history stay isolated to their session

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Backend | Flask (Python) |
| AI Model | Google Gemini (`google-genai` SDK) |
| PDF Reading | PyMuPDF (fitz) |
| Image OCR | EasyOCR |
| Frontend | HTML, CSS (Flask templates) |

---

## 📁 Project Structure

```
Sehat-Vault-AI/
├── app.py                  # Main Flask application & routes
├── gemini_service.py        # Gemini AI client & report analysis logic
├── chatbot.py               # Chatbot logic for follow-up questions
├── pdf_reader.py             # PDF text extraction
├── ocr_reader.py              # Image text extraction (OCR)
├── templates/
│   ├── index.html               # Upload page
│   └── result.html               # Analysis results page
├── requirements.txt
├── .env.example               # Template for environment variables
└── .gitignore
```

---

## 🚀 Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
- Windows: `venv\Scripts\activate`
- Mac/Linux: `source venv/bin/activate`

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Create a `.env` file in the root folder (copy `.env.example` and rename it to `.env`), then add your own API key:
```
GEMINI_API_KEY=your_actual_gemini_api_key
SECRET_KEY=any_random_secret_string
```

Get a free Gemini API key from: https://aistudio.google.com/apikey

6. Run the app:
```bash
python app.py
```

7. Open your browser at: `http://127.0.0.1:8080`

---

## 📌 How It Works

1. User uploads a medical report (PDF or image) on the home page
2. The app extracts text from the file using PyMuPDF (for PDFs) or EasyOCR (for images)
3. The extracted text is sent to Gemini AI, which returns a structured JSON with a summary, abnormal findings, possible diseases, and recommendations
4. Results are displayed on a results page
5. Users can chat with the AI assistant to ask further questions — the assistant only answers based on the uploaded report

---

## ⚠️ Disclaimer

This tool is intended for **informational purposes only** and does **not** provide medical diagnoses or prescriptions. Always consult a qualified healthcare professional for medical advice.

---

## 🔐 Security Note

The `.env` file is intentionally excluded from this repository (see `.gitignore`) to keep API keys private. Each user must create their own `.env` file locally using their own API key.

---

## 👤 Author

**Syed Daniyal Hussain, Azhar Ali & Abdul Raheem**