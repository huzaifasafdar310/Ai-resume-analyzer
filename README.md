# 🤖 AI Resume Analyzer

An AI-powered resume analyzer built with FastAPI + Claude API + Vanilla HTML/CSS/JS.

## Features
- ✅ Paste resume text OR upload PDF
- ✅ Optional job description matching
- ✅ Overall score (0-100) with grade
- ✅ Sub-scores: Skills, Experience, Education, Formatting, Keywords
- ✅ Strengths & Weaknesses breakdown
- ✅ Missing keywords detection
- ✅ Actionable improvement suggestions
- ✅ Job match score & summary
- ✅ Dark cyber-terminal UI

## Tech Stack
- **Frontend:** HTML, CSS, JavaScript (Vanilla)
- **Backend:** Python, FastAPI
- **AI:** Anthropic Claude API
- **PDF Parsing:** pypdf

## Setup

### Backend
```bash
cd backend
pip install -r requirements.txt
export ANTHROPIC_API_KEY=your_api_key_here
python main.py
```

### Frontend
Just open `frontend/index.html` in your browser.
Or serve it:
```bash
cd frontend
python -m http.server 3000
```

## Project Structure
```
resume-analyzer/
├── frontend/
│   └── index.html
├── backend/
│   ├── main.py         # FastAPI routes
│   ├── analyzer.py     # Claude API logic
│   ├── pdf_parser.py   # PDF text extraction
│   └── requirements.txt
└── README.md
```
