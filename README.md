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

## Project Structure

This matches the actual repo layout:

```
Ai-resume-analyzer/
├── index.html        # Frontend UI
├── main.py            # FastAPI app + routes
├── pdf_parser.py       # PDF text extraction
├── requirements.txt
└── README.md
```

## Setup

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY=your_api_key_here
python main.py
```

Then open `index.html` in your browser, or serve it:

```bash
python -m http.server 3000
```

## Live demo

_(add a deployed link here if you have one — Render/Railway/Vercel for the backend, GitHub Pages or Vercel for the frontend)_

## License

MIT
