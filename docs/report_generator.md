# Feature: PDF Report Generator

## Feature Branch
gopi/report-generator

## Purpose
Generates a structured, professionally formatted PDF research report from summarised articles using ReportLab.

## Functions

### generate_report(topic, articles, output_dir)
- Input: research topic, list of summarised articles, output directory
- Output: file path of the generated PDF
- Creates reports/ directory if it does not exist
- Timestamps the filename to avoid overwrites

## Report Structure
1. Title with research topic
2. Generation date and source count
3. Horizontal divider
4. Research summary paragraph
5. Key findings section
6. Each article: title, summary, source URL
7. Footer with author GitHub link

## Dependencies
- reportlab

## Output
- PDF saved to reports/research_YYYYMMDD_HHMMSS.pdf
