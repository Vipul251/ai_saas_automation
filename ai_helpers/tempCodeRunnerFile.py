# gpt_selector_agent.py

from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)  # ✅ use the new client object

def get_selector(field_label, html):
    prompt = f"""
You are an AI agent reading HTML. Find the best CSS selector to locate the field for "{field_label}".
HTML: {html[:4000]}
Return the selector only.
"""
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if available
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print("❌ OpenAI API error:", e)
        # Fallback hardcoded
        if "email" in field_label.lower():
            return 'input[type="email"], input[name="login_email"]'
        elif "password" in field_label.lower():
            return 'input[type="password"]'
        elif "login" in field_label.lower():
            return 'button[type="submit"]'
        else:
            return "input"
