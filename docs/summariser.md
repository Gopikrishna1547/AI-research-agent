# Feature: Text Summarisation Module

## Feature Branch
gopi/summariser

## Purpose
Handles text summarisation using the Hugging Face facebook/bart-large-cnn model. Takes raw article content and returns a concise summary.

## Functions

### get_summariser()
- Loads the BART model once and caches it for reuse
- Prevents reloading the model on every call
- Returns the pipeline object

### summarise_text(text)
- Input: raw article text string
- Output: summarised text string
- Skips summarisation if text is shorter than 100 characters
- Truncates input to 1024 characters to fit model limits

### summarise_articles(articles)
- Input: list of article dictionaries
- Output: list of articles with summary field added
- Calls summarise_text for each article

## Dependencies
- transformers
- torch

## Model Used
- facebook/bart-large-cnn
- Pre-trained on CNN/DailyMail dataset
- Best for news article summarisation
