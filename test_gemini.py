from gemini_service import analyze_report

sample_report = """
Patient Name: Ali
Age: 30

Hemoglobin: 8.5 g/dL
WBC: 13000 /uL
Platelets: 220000 /uL

Impression:
Patient has low hemoglobin and elevated white blood cells.
"""

result = analyze_report(sample_report)

print(result)