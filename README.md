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

## 👤 Author

**Syed Daniyal Hussain & Team**
