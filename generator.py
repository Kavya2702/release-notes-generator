import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_release_notes(data):
    prompt = f"""
    You are a professional release notes generator.

    Generate clean, structured release notes.

    Version: {data['version']}
    Date: {data['date']}
    Features: {data['features']}
    Bug Fixes: {data['bug_fixes']}
    Improvements: {data['improvements']}
    Known Issues: {data['known_issues']}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content
