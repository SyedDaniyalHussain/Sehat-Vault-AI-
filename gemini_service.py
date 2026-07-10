import os
import json
from dotenv import load_dotenv
import google.generativeai as genai
from google.api_core.exceptions import ResourceExhausted

# Load .env
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create Model
model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_report(report_text):

    prompt = f"""
You are an expert medical AI assistant.

Analyze the following medical report.

Return ONLY valid JSON.

Use this exact format:

{{
    "summary":"",

    "abnormal_findings":[
        "",
        ""
    ],

    "possible_diseases":[
        "",
        ""
    ],

    "recommendations":[
        "",
        ""
    ]
}}

Medical Report:

{report_text}

Do not write markdown.
Do not write explanation.
Return only JSON.
"""
    response = model.generate_content(prompt)

    result = response.text

    # remove markdown if Gemini returns ```json
    result = result.replace("```json", "")
    result = result.replace("```", "")

    return json.loads(result)
    # try:
    #     response = model.generate_content(prompt)
    #     return response.text

    # except ResourceExhausted:
    #     return "⚠️ Gemini API quota exceeded. Please wait 1 minute and try again."

    # except Exception as e:
    #     return f"Error: {str(e)}"