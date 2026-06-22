# AI Research Assistant Agent

An AI-powered research agent that searches the web, summarises findings, and generates a structured PDF report automatically.

## How It Works

```
User enters research topic
         |
         v
Tavily API searches the web
         |
         v
Top articles extracted
         |
         v
BART model summarises each article
         |
         v
Structured PDF report generated
         |
         v
User downloads the report
```

## Features

- Real-time web search using Tavily API
- Automatic text summarisation using Hugging Face BART model
- Structured PDF report generation with ReportLab
- Clean Streamlit web interface
- Adjustable number of sources (3-10)
- One-click PDF download

## Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| LangChain | Agent orchestration |
| Tavily API | Real-time web search |
| Hugging Face BART | Text summarisation |
| ReportLab | PDF generation |
| Streamlit | Web interface |

## Project Structure

```
ai-research-agent/
├── src/
│   ├── __init__.py
│   ├── searcher.py              - Web search module
│   ├── summariser.py            - Text summarisation module
│   └── report_generator.py     - PDF report generator
├── tests/
│   └── test_main.py             - Unit tests
├── docs/
│   ├── ARCHITECTURE.md          - System architecture
│   ├── searcher.md              - Searcher module docs
│   ├── summariser.md            - Summariser module docs
│   ├── report_generator.md      - Report generator docs
│   └── streamlit_ui.md          - UI docs
├── reports/                     - Generated reports saved here
├── app.py                       - Main Streamlit interface
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Setup

```bash
git clone https://github.com/Gopikrishna1547/ai-research-agent.git
cd ai-research-agent
pip install -r requirements.txt
cp .env.example .env
# Add your Tavily API key to .env
streamlit run app.py
```

## Branching Strategy

```
main
  └── dev
        └── gopi/web-search
        └── gopi/summariser
        └── gopi/report-generator
        └── gopi/streamlit-ui
        └── gopi/unit-tests
```

## Author

Gopikrishna Bojedla
[LinkedIn](https://www.linkedin.com/in/gopi-krishna-83856320a) | [GitHub](https://github.com/Gopikrishna1547)
