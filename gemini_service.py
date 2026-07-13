import os
import json
from dotenv import load_dotenv
from google import genai

# Load .env
load_dotenv()

# Create Client (new SDK)
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# we are using 2 models becase of limit
# MODEL_NAME = "gemini-3.5-flash"
MODEL_NAME = "gemini-3.1-flash-lite"


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
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    result = response.text

    # remove markdown if Gemini returns ```json
    result = result.replace("```json", "")
    result = result.replace("```", "")

    return json.loads(result)