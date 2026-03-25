from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from analyzer import analyze_resume
from pdf_parser import extract_text_from_pdf
from typing import Optional
import uvicorn

app = FastAPI(title="AI Resume Analyzer")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze(
    resume_text: Optional[str] = Form(None),
    job_description: Optional[str] = Form(None),
    file: Optional[UploadFile] = File(None)
):
    # Extract text from PDF if uploaded
    if file:
        pdf_bytes = await file.read()
        resume_text = extract_text_from_pdf(pdf_bytes)

    if not resume_text:
        return {"error": "No resume text provided"}

    result = await analyze_resume(resume_text, job_description)
    return result

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
