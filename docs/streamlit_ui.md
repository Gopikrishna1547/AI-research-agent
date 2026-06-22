# Feature: Streamlit Web Interface

## Feature Branch
gopi/streamlit-ui

## Purpose
Provides the web interface for the AI Research Assistant Agent. Orchestrates all modules and presents results to the user.

## UI Components

### Input Section
- Text input for research topic
- Slider for number of sources (3-10)
- Run Research Agent button

### Status Section
- Live status updates while agent is working
- Step by step progress display

### Results Section
- Expandable cards for each article
- Article title, summary, and source URL
- First article expanded by default

### Download Section
- Download PDF Report button
- PDF named after research topic

## Flow
1. User enters topic and clicks button
2. Status box shows live progress
3. Results displayed as expandable cards
4. PDF download button appears at bottom

## Dependencies
- streamlit
- All src/ modules
