# Feature: Web Search Module

## Feature Branch
gopi/web-search

## Purpose
Handles all web search functionality using the Tavily API. This module is responsible for searching the web and extracting article data from search results.

## Functions

### search_web(query, max_results)
- Input: research topic string, number of results
- Output: raw search results dictionary from Tavily API
- Error handling: raises exception if API key is missing or API call fails

### extract_articles(search_results)
- Input: raw search results dictionary
- Output: clean list of article dictionaries with title, url, content, score
- Error handling: returns empty list if no results found

## Dependencies
- tavily-python
- python-dotenv

## Environment Variables
- TAVILY_API_KEY: required, get from tavily.com

## Example Output
```
[
  {
    "title": "Latest RAG developments 2025",
    "url": "https://example.com/article",
    "content": "Full article text...",
    "score": 0.95
  }
]
```
