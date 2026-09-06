# 🚀 JobNova AI

JobNova AI is an AI-powered resume analysis and career assistance platform powered by **Ollama** and **Gemma 3**.

It helps users analyze resumes, identify skill gaps, match candidates with jobs, prepare for interviews, and generate AI-powered career insights.


## ✨ Features

- 📄 AI Resume Analyzer
- 🧠 AI Resume Summary
- 🎯 Job & Candidate Matching
- 📊 Skill Gap Analysis
- 💼 Candidate Ranking
- 🎤 Interview Preparation
- 🤖 AI-powered Career Assistance
- 📑 AI-generated Reports


## 🛠️ Technologies Used

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- FastAPI
- Uvicorn

### AI
- Ollama
- Gemma 3 (`gemma3:1b`)

### Other
- PDFPlumber
- Pydantic
- FPDF


# 📋 Requirements

Before running JobNova AI, install:

- Python 3.10 or newer
- Ollama
- Visual Studio Code
- VS Code Live Server extension

---

# 📥 Installation

## 1. Clone the repository

```bash
git clone https://github.com/Varshitha-D1/JobNovaAI.git
cd JobNovaAI
```

## 2. Create a Python virtual environment

### Windows

```powershell
python -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Linux / macOS

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

## 3. Install Python dependencies

With the virtual environment activated:

```bash
pip install -r requirements.txt
```

# 🤖 Ollama Setup

JobNova AI uses Ollama to run the AI model locally.

## 1. Install Ollama

Download and install Ollama from:

https://ollama.com

## 2. Download the required model

Run:

```bash
ollama pull gemma3:1b
```

Check that the model is installed:

```bash
ollama list
```

You should see:

```text
gemma3:1b
```

> **Note:** Ollama must be running for the AI features to work.

---

# ▶️ Running JobNova AI

## Step 1 — Activate the virtual environment

### Windows

```powershell
.\.venv\Scripts\Activate.ps1
```

### Linux / macOS

```bash
source .venv/bin/activate
```

## Step 2 — Start the FastAPI backend

From the project root directory, run:

```bash
python -m uvicorn backend.main:app --reload
```

The backend will normally be available at:

```text
http://127.0.0.1:8000
```

You can also view the FastAPI API documentation at:

```text
http://127.0.0.1:8000/docs
```

## Step 3 — Start the frontend

Open the project in **Visual Studio Code**.

Install the **Live Server** extension if you don't already have it.

Then open:

```text
index.html
```

or the appropriate frontend HTML file and select:

**Right-click → Open with Live Server**

The application will open in your browser.


# 📁 Project Structure

```text
JobNovaAI/
│
├── assets/
│   ├── icons/
│   ├── illustartions/
│   └── logo/
│
├── backend/
│   ├── agents/
│   │   ├── hire_agent.py
│   │   ├── interview_agent.py
│   │   ├── judge_agent.py
│   │   ├── matcher.py
│   │   ├── ranking_agent.py
│   │   ├── reject_agent.py
│   │   ├── report_generator.py
│   │   ├── resume_parser.py
│   │   ├── skill_gap.py
│   │   └── summary_agent.py
│   │
│   └── main.py
│
├── css/
├── js/
├── pages/
├── frontend/
│
├── .gitignore
├── requirements.txt
├── README.md
└── index.html
```


# 🔧 Troubleshooting

### Ollama connection error

Make sure Ollama is installed and running.

Check:

```bash
ollama list
```

If `gemma3:1b` is missing:

```bash
ollama pull gemma3:1b
```

---

### Python package error

Make sure your virtual environment is activated:

```powershell
.\.venv\Scripts\Activate.ps1
```

Then run:

```bash
pip install -r requirements.txt
```


### Backend won't start

Make sure you are running the command from the **JobNovaAI project root**:

```bash
python -m uvicorn backend.main:app --reload
```


### Port 8000 is already in use

Stop the existing FastAPI server with:

```text
Ctrl + C
```

Then start it again.


# 🔒 Security Note

Do not commit passwords, API keys, tokens, or other sensitive information to GitHub.

Environment files such as `.env` are ignored using `.gitignore`.


# 📌 Important

JobNova AI currently runs the AI model **locally through Ollama**.

This means:

- The user needs Ollama installed.
- The required AI model needs to be downloaded.
- AI processing happens locally on the user's computer.


# 🚀 Future Improvements

- Cloud deployment
- User authentication
- Database integration
- Mobile application
- Additional AI models
- Improved resume scoring
- Job recommendation system


## 👨‍💻 Project

**JobNova AI**

AI-powered resume analysis and career assistance.