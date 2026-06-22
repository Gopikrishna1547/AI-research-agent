# Architecture Document — AI Research Assistant Agent

## Overview

The AI Research Assistant Agent is a modular Python application that accepts a research topic, searches the web in real time, summarises findings using a Hugging Face model, and generates a structured PDF report — all through a Streamlit web interface.

---

## System Architecture

```
User (Streamlit UI)
        |
        v
   app.py (orchestrator)
        |
        |---> src/searcher.py        - Tavily API web search
        |---> src/summariser.py      - Hugging Face BART summarisation
        |---> src/report_generator.py - ReportLab PDF generation
        |
        v
   reports/ (output PDF)
```

---

## Data Flow

```
Step 1: User enters topic in Streamlit UI
Step 2: app.py calls searcher.py with the topic
Step 3: searcher.py calls Tavily API and returns articles
Step 4: app.py calls summariser.py with each article
Step 5: summariser.py returns summarised text per article
Step 6: app.py calls report_generator.py with all summaries
Step 7: report_generator.py creates a PDF in reports/
Step 8: Streamlit displays results and offers PDF download
```

---

## Module Responsibilities

| Module | Responsibility |
|---|---|
| app.py | Orchestrates all modules, handles UI |
| src/searcher.py | Web search via Tavily API |
| src/summariser.py | Text summarisation via Hugging Face |
| src/report_generator.py | PDF report generation via ReportLab |
| tests/test_main.py | Unit tests for all modules |

---

## Tech Stack

| Tool | Version | Purpose |
|---|---|---|
| Python | 3.10+ | Core language |
| Streamlit | latest | Web interface |
| Tavily API | latest | Real-time web search |
| Hugging Face Transformers | latest | BART summarisation model |
| ReportLab | latest | PDF generation |
| LangChain | latest | Agent orchestration |
| python-dotenv | latest | Environment variable management |

---

## Environment Variables

| Variable | Description |
|---|---|
| TAVILY_API_KEY | API key from tavily.com |

---

## Error Handling Strategy

- All external API calls wrapped in try/except
- Logging used throughout instead of print statements
- Graceful error messages shown in Streamlit UI
- Empty or failed searches handled without crashing

---

## Future Improvements

- Add ArXiv API for academic paper search
- Add multi-language summarisation support
- Add topic comparison across multiple searches
- Deploy to Streamlit Cloud
- Add caching for repeated searches
