import os
import google.generativeai as genai


def get_model():
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    return genai.GenerativeModel("gemini-2.5-pro")


def prompt_gemini_for_complexity(model, code, metadata):
    prompt = f"""
You're an expert software engineer. Analyze the following Python function for readability and refactoring:

File: {metadata['file']}
Function: {metadata['name']}
Cyclomatic Complexity: {metadata['cyclomatic_complexity']}
Lines: {metadata['start_line']} to {metadata['end_line']}

Code:
{code}

Suggestions:
- Identify code smells
- Recommend simplifications
- Provide reasoning
"""
    response = model.generate_content(prompt)
    return response.text


def prompt_gemini_for_vulnerability(model, code, message):
    prompt = f"""
You're a security expert. Given the following code and semgrep finding:

Semgrep finding: {message}

Code:
{code}

Explain the vulnerability, its potential risk, and suggest a fix.
"""
    response = model.generate_content(prompt)
    return response.text
