import logging
import os
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()
log = logging.getLogger(__name__)


def search_web(query: str, max_results: int = 5) -> dict:
    """Search the web for a given query using Tavily API."""
    log.info(f"Searching web for: {query}")
    client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
    results = client.search(
        query=query,
        max_results=max_results,
        include_answer=True,
        include_raw_content=False
    )
    log.info(f"Found {len(results['results'])} results")
    return results


def extract_articles(search_results: dict) -> list:
    """Extract article titles, urls and content from search results."""
    articles = []
    for r in search_results.get("results", []):
        articles.append({
            "title": r.get("title", "No title"),
            "url": r.get("url", ""),
            "content": r.get("content", ""),
            "score": r.get("score", 0)
        })
    return articles
