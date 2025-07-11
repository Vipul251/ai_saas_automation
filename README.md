# 🚀 AI SaaS Automation

This project automates data scraping and interaction with SaaS admin portals using AI and browser automation.

## 📌 Project Description

`ai_saas_automation` is an AI-driven tool that combines **Large Language Models (LLMs)** with **RPA (Robotic Process Automation)** to:
- Log into SaaS platforms (like admin dashboards)
- Scrape user details (e.g., names, emails, last login)
- Use AI (OpenAI/GPT) to dynamically identify page elements via selectors

The goal is to enable **hands-free user data extraction** for companies managing multiple SaaS tools that don’t provide APIs.

---

## 🧠 Key Features

- 🔍 **AI-Driven Selector Detection**: Uses GPT-4o to find the correct CSS selectors from HTML dynamically.
- 🧭 **Playwright Automation**: Automates browser login and scraping via headless Chromium.
- 🔐 **Environment Variables**: Keeps sensitive data like API keys and login credentials secure in `.env`.
- 📊 **CSV Output**: Extracted session/user data is stored in `login_sessions.csv`.
- 📁 **Modular Code**: Easy to extend and scale with `ai_helpers/` and `browsers/` modules.

---

## 📁 Project Structure

ai_saas_automation/
├── .env # API keys and secrets
├── .gitignore
├── app.py # Main entrypoint script
├── requirements.txt # Python dependencies
├── login_sessions.csv # Output file
│
├── ai_helpers/
│ ├── init.py
│ ├── gpt_selector_agent.py # GPT model for field selector inference
│
├── browsers/
│ ├── init.py
│ ├── playwright_controller.py # Automation logic using Playwright

yaml
Copy
Edit

---

## 🔧 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/your-username/ai_saas_automation.git
cd ai_saas_automation
2. Create & activate virtual environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate   # On Windows
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Add your .env file
Create a .env file in the root:

ini
Copy
Edit
OPENAI_API_KEY=your_openai_key_here
🚀 Run the App
bash
Copy
Edit
python app.py
You should see output like:

vbnet
Copy
Edit
🔑 API Key Loaded: True
🚀 Starting SaaS Automation...
✅ Automation completed!
If you want to test without OpenAI:

bash
Copy
Edit
python app.py --demo
🧪 Demo Output
Check login_sessions.csv for scraped user data such as:

Name	Email	Last Login
Alice Doe	alice@example.com	2024-05-01
Bob Smith	bob@example.org	2024-04-28
