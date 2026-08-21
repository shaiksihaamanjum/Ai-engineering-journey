# 🤖 AI Chatbot

A simple AI chatbot built with **Google Gemini, Python, Pydantic, JSON, and Streamlit**.

## 🚀 Features

* Gemini-powered chatbot
* Conversation memory using `previous_interaction_id`
* Structured JSON output
* Pydantic validation
* Streamlit GUI
* Basic API rate-limit handling

## 📁 Structure

```text
AI_Chatbot/
├── gui_code.py      # streamlit GUI
├── main.py         # Normal chatbot
├── .env            # API key
├── .gitignore
└── README.md
|__ pyproject.toml
```

## ⚙️ Setup

```bash
pip install google-genai python-dotenv pydantic streamlit
```

Create `.env`:

```text
my_api_key=YOUR_GEMINI_API_KEY
```

## 💻 Run

### Normal chatbot

```bash
python chatbot.py
```

### GUI

```bash
streamlit run main.py
```

Then open:

```text
http://localhost:8501
```

## 🧠 Core Concepts

```text
User
 ↓
Gemini API
 ↓
Structured JSON
 ↓
Pydantic
 ↓
Python Object
 ↓
GUI / Terminal
```

**Technologies:** Python • Gemini API • JSON • Pydantic • Streamlit
