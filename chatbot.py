# from gemini_service import model


# def chat_with_report(report_text, chat_history, user_message):
#     """
#     Generates chatbot response using the uploaded medical report
#     and previous conversation.
#     """

#     history = ""

#     if chat_history:
#         for chat in chat_history:
#             history += f"User: {chat['user']}\n"
#             history += f"Assistant: {chat['assistant']}\n"

#     prompt = f"""
# You are Sehat Vault AI.

# You are a medical report assistant.

# IMPORTANT RULES

# 1. ONLY answer questions related to the uploaded medical report.

# 2. NEVER make up information.

# 3. If the answer is not present inside the report, clearly say:

# "I couldn't find that information in your uploaded report."

# 4. Explain everything in simple language.

# 5. Do NOT diagnose diseases.

# 6. Do NOT prescribe medicines.

# 7. Recommend consulting a healthcare professional whenever appropriate.

# 8. If the user asks anything unrelated to the report,
# politely say:

# "I can only answer questions about your uploaded medical report."

# =========================
# MEDICAL REPORT
# =========================

# {report_text}

# =========================
# PREVIOUS CONVERSATION
# =========================

# {history}

# =========================
# CURRENT USER QUESTION
# =========================

# {user_message}

# Answer naturally and briefly.
# """

#     try:
#         response = model.generate_content(prompt)

#         return response.text.strip()

#     except Exception as e:
#         return f"Error: {str(e)}"



from gemini_service import client, MODEL_NAME


def chat_with_report(report_text, chat_history, user_message):
    """
    Generates chatbot response using the uploaded medical report
    and previous conversation.
    """

    history = ""

    if chat_history:
        for chat in chat_history:
            history += f"User: {chat['user']}\n"
            history += f"Assistant: {chat['assistant']}\n"

    prompt = f"""
You are Sehat Vault AI.

You are a medical report assistant.

IMPORTANT RULES

1. ONLY answer questions related to the uploaded medical report.

2. NEVER make up information.

3. If the answer is not present inside the report, clearly say:

"I couldn't find that information in your uploaded report."

4. Explain everything in simple language.

5. Do NOT diagnose diseases.

6. Do NOT prescribe medicines.

7. Recommend consulting a healthcare professional whenever appropriate.

8. If the user asks anything unrelated to the report,
politely say:

"I can only answer questions about your uploaded medical report."

=========================
MEDICAL REPORT
=========================

{report_text}

=========================
PREVIOUS CONVERSATION
=========================

{history}

=========================
CURRENT USER QUESTION
=========================

{user_message}

Answer naturally and briefly.
"""

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        return response.text.strip()

    except Exception as e:
        return f"Error: {str(e)}"